from django.urls import path
from .views import get_retail_items, get_consignment_items

urlpatterns = [
    path('', get_retail_items, name='retail'),
    path('consigned', get_consignment_items, name='consigned'),
]
