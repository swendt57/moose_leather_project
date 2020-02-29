from django.shortcuts import get_object_or_404
from products.models import Item


def cart_contents(request):
    """Allows the cart to be displayed anywhere in the app"""

    cart = request.session.get('cart', {})



    cart_items = []
    total = 0
    item_count = 0

    for identifier, quantity in cart.items():
        item = get_object_or_404(Item, pk=identifier)
        total += quantity * item.price
        item_count += quantity
        cart_items.append({'id': identifier, 'quantity': quantity, 'item': item})

    # for x in cart_items:
    #     print(c)

    return {'cart_items': cart_items, 'total': total, 'item_count': item_count}