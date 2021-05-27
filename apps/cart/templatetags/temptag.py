from django import template

from apps.cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True, name="in_cart")
def in_cart(context, id):
    request = context['request']
    cart = Cart(request)
    return {
        "in_cart": cart.has_product(id),
        "count": cart.get_product_quantity(id)
    }
