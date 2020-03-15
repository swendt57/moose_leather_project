from django.shortcuts import render
from products.models import Item


def get_proper_grammar(count):
    """As the name implies"""
    if count == 1:
        return "result was"
    else:
        return "results were"


def do_search(request):
    """Searches for q in Item titles"""
    q = request.GET['q']
    page_type = request.GET['type']

    if page_type == 'retail':
        found_items = Item.objects.filter(title__icontains=q, is_consignment__exact=False)
        other_count = Item.objects.filter(title__icontains=q, is_consignment=True).count()
    else:
        found_items = Item.objects.filter(title__icontains=q, is_consignment__exact=True)
        other_count = Item.objects.filter(title__icontains=q, is_consignment=False).count()

    forward_page = page_type + "_items.html"
    page_value = "." + page_type

    return render(request, forward_page, {'page_items': found_items, 'page_title': 'Search Results',
                                          'page_heading': 'Search Results', 'page': page_value, "other_count": other_count})
