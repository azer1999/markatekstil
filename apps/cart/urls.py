from django.urls import path

from apps.cart.views import api_add_to_cart, api_remove_from_cart,CartView

app_name = 'cart'

urlpatterns = [
    path('api/add_to_cart/', api_add_to_cart, name='add-to-cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='remove-from-cart'),
    path('', CartView.as_view(), name='cart'),
]
