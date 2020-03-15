from django.db import models
from django.contrib.auth.models import User


class ShippingInfo(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    address1 = models.CharField(max_length=50, blank=False, null=False)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=25, blank=False, null=False)
    postal_code = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_info = models.ForeignKey(ShippingInfo, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name