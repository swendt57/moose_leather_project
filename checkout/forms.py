from django import forms
from orders.models import Order


class MakePaymentForm(forms.Form):
    """Creates the credit card charge form"""
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    # These are set to 'required=False' so that the plain text is not transmitted through the browser.
    # Stripe handles this themselves
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiration Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiration Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """Creates the order form to collect user details"""
    save_address = forms.BooleanField(label='Save/update my address for future use', required=False)

    class Meta:
        model = Order
        widgets = {'total': forms.HiddenInput(), 'address2': forms.TextInput(attrs={'placeholder': 'Optional'})}
        labels = {'address1': 'Address', 'address2': 'Address 2', 'postal_code': 'Postal Code',
                  'order_info': 'Special Instructions'}
        placeholders = {'address2': 'Optional', 'order_info': 'Optional'}
        fields = (
            'name', 'address1', 'address2', 'city', 'state', 'postal_code', 'phone', 'order_info', 'total',
            'save_address'
        )
