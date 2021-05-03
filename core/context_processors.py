from django.contrib.sites.shortcuts import get_current_site

from apps.cart.cart import Cart
from apps.product.models import Category
from core.forms import ContactFeedbackForm, SubscribeForm
from core.models import SocialMedia, Logo, ContactInfo, FAQ


def main(request):
    context = {}
    subscribe_form = SubscribeForm()
    context["media"] = SocialMedia.objects.all()
    context["cart"] = Cart(request)
    context["subscribe_form"] = subscribe_form
    context["logo"] = Logo.on_site.last()
    context['categories'] = Category.objects.all()
    context['categories_'] = Category.objects.filter(parent=None).all()
    context['current_site'] = get_current_site(request)

    return context
