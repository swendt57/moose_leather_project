from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from annoying.functions import get_object_or_None
from .forms import MakePaymentForm, OrderForm
from orders.models import LineItem
from accounts.models import ShippingInfo
from django.conf import settings
from datetime import datetime
from products.models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """Checks out the user - processes payment and saves the order to the database"""
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        charge_info = None

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = datetime.now()
            # don't save yet - wait for charge to clear...

            cart = request.session.get('cart', {})
            total = 0
            line_items = []

            for id, quantity in cart.items():
                item = get_object_or_404(Item, pk=id)
                total += quantity * item.price
                order_line_item = LineItem(
                    order=order,
                    item=item,
                    quantity=quantity,
                    price=item.price,
                    is_consignment=item.is_consignment
                )
                line_items.append(order_line_item)
                # don't save yet - wait for charge to clear...

            try:
                charge_info = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, your card was declined")

            # refactor code so that this is skipped if the card is declined. Currently, the app is posting the
            #  error message above as well as the one below. Then you can remove the 'charge_info is not None' in the if

            if charge_info is not None and charge_info.paid:

                # charge was successful, so NOW save all pending objects
                order.save()
                for li in line_items:
                    li.save()

                # If save address checked, create or update shipping info table
                if order_form.data.get('save_address') == 'on':
                    create_or_update_shipping_info(request, order)

                messages.success(request, "You have successfully paid! Thank you for your business!")
                request.session['cart'] = {}
                return redirect(reverse('retail'))
            else:
                messages.error(request, "We are unable to take payment")
        else:
            print("Payment form errors: " + payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        # pre-populate the shipping info if it exists
        order_form = populate_and_or_return_order_form(request)

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE,
                   'page_title': 'Checkout', 'page_heading': 'Shipping and Payment Details', 'page': '.tbd'})


def populate_and_or_return_order_form(request):
    """If user has shipping info record, pre-populate the form"""

    shipping_info = get_object_or_None(ShippingInfo, user_id=request.user.id)

    if shipping_info is not None:
        order_form = OrderForm(initial={
            'name': shipping_info.name,
            'address1': shipping_info.address1,
            'address2': shipping_info.address2,
            'city': shipping_info.city,
            'state': shipping_info.state,
            'postal_code': shipping_info.postal_code,
            'phone': shipping_info.phone
        })
    else:
        order_form = OrderForm()

    return order_form


def create_or_update_shipping_info(request, order):
    """Creates a new, or updates an existing, shipping info record"""

    # Check to see if shipping info exists for this user
    shipping_info = get_object_or_None(ShippingInfo, user_id=request.user.id)
    new_shipping_info = ShippingInfo(
        user_id=request.user.id,
        name=order.name,
        address1=order.address1,
        address2=order.address2,
        city=order.city,
        state=order.state,
        postal_code=order.postal_code,
        phone=order.phone
    )

    # if a record already exists, update it. otherwise create a new one
    if shipping_info is not None:
        new_shipping_info.id = shipping_info.id
    new_shipping_info.save()

