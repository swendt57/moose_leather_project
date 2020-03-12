from django.shortcuts import render
from django.contrib import messages
from products.models import Item


def get_proper_grammar(count):
    if count == 1:
        return "result was"
    else:
        return "results were"


def do_search(request):
    q = request.GET['q']
    page_type = request.GET['type']
    if page_type == 'retail':
        page_name = "New Goods"
    else:
        page_name = "Consigned Goods"

    if page_type == 'retail':
        found_items = Item.objects.filter(title__icontains=q, is_consignment__exact=False)
        other_count = Item.objects.filter(title__icontains=q, is_consignment=True).count()
    else:
        found_items = Item.objects.filter(title__icontains=q, is_consignment__exact=True)
        other_count = Item.objects.filter(title__icontains=q, is_consignment=False).count()

    forward_page = page_type + "_items.html"
    page_value = "." + page_type

    # messages.info(request, str(other_count) + " additional " + get_proper_grammar(other_count) + " found on the <a class=\"alert-link\" href=\"\?type=" + page_type + "&q=" + q + "\">" + page_name + "\</a\> page.")

    return render(request, forward_page, {'found_items': found_items, 'page_title': 'Search Results',
                                          'page_heading': 'Search Results', 'page': page_value, "other_count": other_count})
