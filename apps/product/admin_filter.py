from datetime import date

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.product.models import Product


class PriceRangeFilterAdmin(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Qiymət Aralığı')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0-1000', _('0-1000 AZN')),
            ('1000-2000', _('1000-2000 AZN')),
            ('2000-3000', _('2000-3000 AZN')),
            ('3000-4000', _('3000-4000 AZN')),
            ('5000-10000', _('5000-10000 AZN')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():
            return Product.objects.filter(price__range=[int(i) for i in self.value().split('-')])


class AtDiscountFilterAdmin(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Endirimdə')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'discount'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('yes', _('Bəli')),
            ('no', _('Xeyr')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'yes':
            return Product.objects.filter(old_price__isnull=False).all()
        if self.value() == 'no':
            return Product.objects.filter(old_price=None).all()
