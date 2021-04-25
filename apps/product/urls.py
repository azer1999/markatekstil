from django.urls import path

from apps.product.views import ProductView, ProductsCategoryDetailView,ProductsDetailView

app_name = 'products'

urlpatterns = [
    path('mehsullar/', ProductView.as_view(), name='products'),
    path('mehsullar/kateqoriyalar/<slug>/', ProductsCategoryDetailView.as_view(), name='products-category'),
    path('mehsul/<slug>/', ProductsDetailView.as_view(), name='product-detail')
]
