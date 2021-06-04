# Create your views here.
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from apps.cart.cart import Cart
from apps.product.models import Product, Category


class ProductView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 9

    def get_queryset(self):
        if 'name' in self.request.GET:
            return Product.objects.filter(title__icontains=self.request.GET.get('name'), site=settings.SITE_ID)
        else:
            queryset = Product.objects.filter(site=settings.SITE_ID)
            return queryset


class ProductsCategoryDetailView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category__in=category.get_descendants(include_self=True),
                                      site=settings.SITE_ID)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_category'] = get_object_or_404(Category, slug=(self.kwargs['slug']))
        return context


class ProductsDetailView(DetailView):
    model = Product
    template_name = "product-item.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
