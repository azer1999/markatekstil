from django.contrib import admin

# Register your models here.
from apps.order.models import Order, OrderItem


class OrderItemInlineAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInlineAdmin]
    list_display = ('id','first_name','last_name','email','phone','city','address','get_total_cost','created')
    list_filter = ('created',)
