from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, StackedInline
from mptt.admin import MPTTModelAdmin

from apps.product.models import Product, Category, ProductImage, ProductProperty, ProductPlan, ProductLabel


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductPropertyAdminInline(StackedInline):
    model = ProductProperty


class ProductPlanAdminInline(StackedInline):
    model = ProductPlan

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductImageInline, ProductPropertyAdminInline,ProductPlanAdminInline]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(ProductLabel)
