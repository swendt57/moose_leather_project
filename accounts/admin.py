from django.contrib import admin
from .models import UserProfile, ShippingInfo

admin.site.register(UserProfile)
admin.site.register(ShippingInfo)
