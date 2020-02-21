from django.shortcuts import render
from .models import Item, Category, Size


def get_retail_items(request):
    retail_items = Item.objects.filter(is_consignment__exact=False)
    return render(request, 'retail_items.html', {'retail_items': retail_items, 'page_title': 'Moose Leather',
                                                 'page_heading': 'New Goods', 'page': '.retail'})


def get_consignment_items(request):
    consigned_items = Item.objects.filter(is_consignment__exact=True)
    return render(request, 'consigned_items.html', {'consigned_items': consigned_items, 'page_title': 'Moose Leather',
                                                    'page_heading': 'Consignment', 'page': '.consigned'})