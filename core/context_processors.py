from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

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
    context['categories'] = Category.objects.filter(site=settings.SITE_ID).all()
    context['categories_'] = Category.objects.filter(parent=None, site=settings.SITE_ID)
    context['current_site'] = get_current_site(request)
    context['sites'] = Site.objects.all()

    return context
