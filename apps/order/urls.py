from django.urls import path

from apps.order.views import OrderView

app_name = 'order'

urlpatterns = [
    path('', OrderView.as_view(), name='checkout'),
]
