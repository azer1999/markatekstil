from django.urls import path

from apps.user.views import SignUpView
from apps.cart.views import api_add_to_cart, api_remove_from_cart

app_name = 'account'

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
]
