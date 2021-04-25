from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json

from .cart import Cart
from ..product.models import Product


def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (
            product.id, product.title, product.price, item['quantity'], item['total_price'], product.get_thumbnail, url,
            product.num_available)

        productsstring = productsstring + b

    context = {}
    context['cart'] = cart
    return render(request, 'cart.html', context)


def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'success.html')


def api_add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    cart = Cart(request)
    jsonresponse = {'success': True, 'quantity': cart.get_product_quantity(product_id)}
    return JsonResponse(jsonresponse)


def api_remove_from_cart(request):
    data = json.loads(request.body)

    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)
    jsonresponse = {'success': True}
    return JsonResponse(jsonresponse)
