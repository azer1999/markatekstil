from django.urls import path

from apps.product.views import ProductView, ProductsCategoryDetailView,ProductsDetailView

app_name = 'products'

urlpatterns = [
    path('<str:domain>/mehsullar/', ProductView.as_view(), name='products'),
    path('<str:domain>/kateqoriyalar/<slug>/', ProductsCategoryDetailView.as_view(), name='products-category'),
    path('<str:domain>/mehsul/<slug>/', ProductsDetailView.as_view(), name='product-detail')
]
