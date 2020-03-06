from django.shortcuts import render
from products.models import Item, Category


def do_search(request):
    retail_items = Item.objects.filter(title__icontains=request.GET['q'])
    return render(request, 'retail_items.html', {'retail_items': retail_items, 'page_title': 'Moose Leather',
                                                 'page_heading': 'Search Results', 'page': '.retail'})
