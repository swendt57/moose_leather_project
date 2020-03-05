from django.db import models
from products.models import Item, Size
from accounts.models import ShippingInfo
from datetime import datetime


class Order(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    address1 = models.CharField(max_length=50, blank=False, null=False)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=25, blank=False, null=False)
    postal_code = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    order_info = models.CharField(max_length=200, null=True, blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    date = models.DateTimeField(blank=True, null=True, default=datetime.now)

    def __str__(self):
        return self.name


class LineItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL)  # required for retail sale
    is_consignment = models.BooleanField(null=False, default=False)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name
