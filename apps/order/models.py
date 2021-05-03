from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('base_user.MyUser',related_name='user_orders', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(_('Ad'),max_length=50)
    last_name = models.CharField(_('Soyad'),max_length=50)
    phone = models.CharField(_('Əlaqə Nömrəsi'),max_length=15)
    email = models.EmailField(_('E-poçt'))
    address = models.CharField(_('Adres'),max_length=250)
    city = models.CharField(_('Şəhər'),max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Sifariş')
        verbose_name_plural = _('Sifarişlər')

    def __str__(self):
        return f'{_("Sifariş")} - {self.id}'

    @property
    @admin.display(description=_("Ümumi Qiymət"))
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_total_item_cost(self):
        return self.price * self.quantity
