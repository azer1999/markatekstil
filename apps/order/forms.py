from django import forms

from apps.order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("email","first_name", "last_name","phone","address","city")

    field_order = ['first_name', 'last_name', 'email', 'phone','city','address']
