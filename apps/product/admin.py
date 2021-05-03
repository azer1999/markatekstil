from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from django.contrib.admin import ModelAdmin, StackedInline
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin

from apps.product.admin_filter import PriceRangeFilterAdmin, AtDiscountFilterAdmin
from apps.product.models import Product, Category, ProductImage, ProductProperty, ProductPlan, ProductLabel


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductPropertyAdminInline(StackedInline):
    model = ProductProperty


class ProductPlanAdminInline(StackedInline):
    model = ProductPlan


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductImageInline, ProductPropertyAdminInline, ProductPlanAdminInline]
    empty_value_display = '-empty-'
    list_display = ('title', 'category', 'price', 'old_price', 'image_tag', 'site',)
    list_editable = ('price', 'old_price', 'site',)
    list_display_links = ('title',)

    list_filter = (AtDiscountFilterAdmin, PriceRangeFilterAdmin, 'site',)
    search_fields = ['title', 'brief_info', ]

    @admin.display(description=_("Şəkil"))
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_thumbnail()))




admin.site.register(Category, MPTTModelAdmin)
admin.site.register(ProductLabel)
