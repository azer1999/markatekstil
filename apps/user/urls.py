from django.urls import path

from apps.user.views import SignUpView, activate, ProfileView, LoginView, LogoutView
from apps.cart.views import api_add_to_cart, api_remove_from_cart

app_name = 'user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
