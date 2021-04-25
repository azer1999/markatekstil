from apps.cart.cart import Cart
from apps.product.models import Category
from core.forms import ContactFeedbackForm, SubscribeForm
from core.models import SocialMedia, Logo, ContactInfo, FAQ


def main(request):
    context = {}
    contact_form = ContactFeedbackForm()
    subscribe_form = SubscribeForm()
    context["media"] = SocialMedia.objects.all()
    context["cart"] = Cart(request)
    context["faq"] = FAQ.objects.all()
    context["contact_form"] = contact_form
    context["subscribe_form"] = subscribe_form
    context["logo"] = Logo.objects.last()
    context["contact_info"] = ContactInfo.objects.last()
    context['categories'] = Category.objects.all()
    context['categories_'] = Category.objects.filter(parent=None).all()

    return context
