from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from django.contrib.admin import ModelAdmin, StackedInline
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from apps.product.admin_filter import PriceRangeFilterAdmin, AtDiscountFilterAdmin
from apps.product.models import Product, Category, ProductImage, ProductProperty, ProductLabel, ProductSize


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductPropertyAdminInline(StackedInline):
    model = ProductProperty


class ProductSizeAdminInline(StackedInline):
    model = ProductSize


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductSizeAdminInline, ProductImageInline, ProductPropertyAdminInline]
    empty_value_display = '-empty-'
    list_display = ('title', 'category', 'image_tag', 'site',)
    list_editable = ('site',)
    list_display_links = ('title',)

    list_filter = (AtDiscountFilterAdmin, PriceRangeFilterAdmin, 'site',)
    search_fields = ['title', 'brief_info', ]

    @admin.display(description=_("Şəkil"))
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_thumbnail()))


admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(ProductLabel)
