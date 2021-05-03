from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View

from apps.base_user.models import MyUser
from apps.cart.cart import Cart
from apps.order.forms import OrderForm
from apps.order.models import OrderItem
from core.tools import get_or_none


class OrderView(View):
    template_name = 'checkout.html'
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        order_form = self.form_class(request.POST)
        if order_form.is_valid:
            user = get_or_none(MyUser, id=request.user.id)
            order = order_form.save(commit=False)
            order.user = user
            order.save()
            cart = Cart(request)
            for i in cart:
                item = OrderItem.objects.create(
                    order=order,
                    product=i['product'],
                    price=i['price'],
                    quantity=i['quantity']
                )
                item.save()
            cart.clear()
            messages.add_message(request, messages.INFO,
                                 _("Sifarişiniz qeydə alındı.Sizinlə yaxın müddətdə əlaqə qurulacaq"))
            return redirect(reverse('core:index',args=(get_current_site(request).name,)))
        else:
            return redirect(reverse('core:index',args=(get_current_site(request).name,)))

    def get(self, request, *args, **kwargs):
        context = {}
        context["order_form"] = self.form_class
        return render(request, self.template_name, context)
