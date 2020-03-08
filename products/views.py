from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Item
from .forms import ConsignmentForm


def get_retail_items(request):
    """Displays all retail goods for sale"""
    retail_items = Item.objects.filter(is_consignment__exact=False)

    return render(request, 'retail_items.html', {'retail_items': retail_items, 'page_title': 'Moose Leather',
                                                 'page_heading': 'New Goods', 'page': '.retail'})


def get_consignment_items(request):
    """Displays all consigned goods for sale"""
    consigned_items = Item.objects.filter(is_consignment__exact=True)

    return render(request, 'consigned_items.html', {'consigned_items': consigned_items, 'page_title': 'Moose Leather',
                                                    'page_heading': 'Consigned Goods', 'page': '.consigned'})


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
        # TODO do I need this if I have separate methods for displaying and submitting the form?
        form = ConsignmentForm(None)
        return render(request, 'upload_consigned_item.html', {'consignment_form': form,
                                                              'page_title': 'Upload Item',
                                                              'page_heading': 'Sell Something',
                                                              'page': '.consigned'})

def load_comments(request):
    """Displays the Disqus comments page"""

    return render(request, 'comments.html', {'page_title': 'Comments', 'page_heading': 'Comments', 'page': '.tbd'})