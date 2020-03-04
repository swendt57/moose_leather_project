from django.contrib import admin
from orders.models import Order, LineItem


class OrderLineAdminInline(admin.TabularInline):
    model = LineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
