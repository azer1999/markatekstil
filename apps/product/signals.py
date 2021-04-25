# Reservations Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.product.models import Product, ProductProperty


@receiver(post_save, sender=Product)
def on_product_created(sender, instance, created, **kwargs):
    if created:
        kw = [
            {"field": "Ümumi sahə", "content": ""},
            {"field": "Otaq sayı", "content": ""},
            {"field": "Elektrik işləri", "content": ""},
            {"field": "İzolyasiya", "content": ""},
            {"field": "Divar və tavan", "content": ""},
            {"field": "Döşəmə", "content": ""},
            {"field": "Pəncərə", "content": ""},
            {"field": "Pəncərə sayı	", "content": ""},
            {"field": "Pəncərə ölçüləri", "content": ""},
            {"field": "Qapı", "content": ""},
            {"field": "Qapı ölçüləri", "content": ""}
        ]
        for i in kw:
            data_property = ProductProperty.objects.create(**i)
            data_property.product = instance
            data_property.save()
