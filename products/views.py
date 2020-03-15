from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from .models import Item
from .forms import ConsignmentForm
from datetime import datetime
from pathlib import Path


def get_items_per_page(request):
    """Returns the number of panels to display per page on different screen sizes"""
    screen_width = int(request.session.get('screen-width'))
    if screen_width >= 1024:
        return 3
    elif 640 <= screen_width < 1024:
        return 2
    else:
        return 4  # don't add too much pagination to portrait phones


def get_retail_items(request):
    """Displays all retail goods for sale"""
    found_items = Item.objects.filter(is_consignment__exact=False).order_by('title')

    page_number = request.GET.get('page', 1)
    paginator = Paginator(found_items, get_items_per_page(request))
    page_items = paginator.page(page_number)

    return render(request, 'retail_items.html', {'page_items': page_items,
                                                 'page_title': 'Moose Leather',
                                                 'page_heading': 'New Goods',
                                                 'page': '.retail'})


def get_consignment_items(request):
    """Displays all consigned goods for sale"""
    found_items = Item.objects.filter(is_consignment__exact=True).order_by('title')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(found_items, get_items_per_page(request))
    page_items = paginator.page(page_number)

    return render(request, 'consigned_items.html', {'page_items': page_items,
                                                    'page_title': 'Moose Leather',
                                                    'page_heading': 'Consigned Goods',
                                                    'page': '.consigned'})


def test_consignment(item):
    """Checks to see if the Item is consigned"""
    if not item.is_consignment:
        return '.retail'
    else:
        return '.consigned'


def get_item_details(request):
    """Displays the Details page for the requested item"""
    item = Item.objects.get(id=request.GET.get('id'))
    return render(request, 'item_details.html', {'item': item,
                                                 'page_title': 'Moose Leather',
                                                 'page_heading': 'History and Background',
                                                 'page': test_consignment(item),
                                                 'CANONICAL_URL_DETAILS': settings.CANONICAL_URL_DETAILS})


@login_required
def render_consigned_item_upload(request):
    """Displays the form for a user to upload a consigned item"""
    consignment_form = ConsignmentForm
    return render(request, 'upload_consigned_item.html', {'consignment_form': consignment_form,
                                                          'page_title': 'Upload Item',
                                                          'page_heading': 'Sell Something',
                                                          'page': '.consigned'})


@login_required
def submit_consigned_item(request):
    """Validates and submits the consigned item or returns the user back to the form if unable to process"""
    if request.method == 'POST':
        form = ConsignmentForm(request.POST, request.FILES)

        if form.is_valid() and request.user.is_authenticated:
            item = form.save(commit=False)
            item.user = request.user
            item.is_consignment = True

            # rename the image to avoid overwriting files
            new_filename = assemble_new_filename(request, item.image.name)
            item.image.name = new_filename

            item.save()
            messages.success(request, "Your upload was successful!")

            return redirect(reverse('consigned'))
        else:
            messages.error(request, "Unable to process your upload. Please see error messages below.")

            return render(request, 'upload_consigned_item.html', {'consignment_form': form,
                                                                  'page_title': 'Upload Item',
                                                                  'page_heading': 'Sell Something',
                                                                  'page': '.consigned'})
    else:
        form = ConsignmentForm(None)
        return render(request, 'upload_consigned_item.html', {'consignment_form': form,
                                                              'page_title': 'Upload Item',
                                                              'page_heading': 'Sell Something',
                                                              'page': '.consigned'})


def assemble_new_filename(request, filename):
    """Renames the uploaded image to avoid overwriting other user's files"""
    now = datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    name = request.user.last_name
    ext = Path(filename).suffix

    return name + timestamp + ext
