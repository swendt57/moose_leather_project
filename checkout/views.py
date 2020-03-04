from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from orders.models import LineItem
from django.conf import settings
from datetime import datetime
from products.models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        customer = None

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = datetime.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                item = get_object_or_404(Item, pk=id)
                total += quantity * item.price
                order_line_item = LineItem(
                    order=order,
                    item=item,
                    quantity=quantity,
                    price=item.price
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, your card was declined")

            # TODO refactor code so that this is skipped if the card is declined. Currently, the app is posting the
            #  error message above as well as the one below. Then you can take out the 'customer is not None' check
            if customer is not None and customer.paid:
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
        order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
