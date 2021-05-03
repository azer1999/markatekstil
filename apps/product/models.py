from io import BytesIO

from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.core.files import File
from PIL import Image
from colorfield.fields import ColorField
import math
# Create your models here.
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from core.tools import slugify


class Category(MPTTModel):
    name = models.CharField(_("Kateqoriya Adı"), max_length=100)
    image = models.ImageField(_("Şəkil"), upload_to='category/images/')
    slug = models.SlugField(_("Slug"), blank=True, unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name=_("Ana Kateqoriya")
    )

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
            ancestors = [i.name for i in ancestors]
        except:
            ancestors = [self.name]

        return ' > '.join(ancestors[:len(ancestors) + 1])

    class Meta:
        verbose_name = _('Kateqoriya')
        verbose_name_plural = _('Kateqoriyalar')

    def has_children(self):
        return True if (self.get_children().count() > 0) else False

    def get_absolute_url(self):
        return reverse("products:products-category", kwargs={
            'slug': self.slug,
            'domain': self.site.name
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_category_products(self):
        return Product.objects.filter(category__in=self.get_descendants(include_self=True))


class ProductLabel(models.Model):
    color = ColorField(_("Rəng Seçin"), default='#FF0000')
    text = models.CharField(_("Etiket"), max_length=20)

    class Meta:
        verbose_name = _("Etiket")
        verbose_name_plural = _("Etiketlər")

    def __str__(self):
        return f'{self.text}'


class Product(models.Model):
    labels = models.ManyToManyField(ProductLabel, related_name="product_labels")

    image = models.ImageField(_("Məhsul Şəkili"), upload_to='products/images/',
                              help_text=_("Tövsiyə olunan şəkil dəyəri - 800x600"))
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True, null=True)

    title = models.CharField(_("Məhsul Başlıqı"), max_length=100)
    brief_info = models.TextField(_("Qısa Məlumat"), max_length=100)
    content = RichTextField(_("Məhsul Məzmunu"))
    category = TreeForeignKey(Category, on_delete=models.CASCADE, related_name="category_products")
    slug = models.SlugField(_("Slug"), blank=True, unique=True)
    price = models.PositiveIntegerField(_("Məhsul Qiyməti"))
    old_price = models.PositiveIntegerField(_("Köhnə Qiymət"), help_text=_(
        "Məhsulun ENDİRİMDƏ olması üçün köhnə qiymət yeni qiymətdən çox olmalidir!"),null=True,blank=True)

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Məhsul")
        verbose_name_plural = _("Məhsullar")

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={
            'slug': self.slug,
            'domain': self.site.name
        })

    def get_related_products(self):
        return Product.objects.filter(category__in=self.category.get_descendants(include_self=True)).exclude(pk=self.pk).all()[:20]

    def get_discount(self):
        if self.old_price:
            print(self.price * 100 / self.old_price - 100)
            return math.ceil(self.price * 100 / self.old_price - 100)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(90, 90)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()

        if img.mode == "JPEG":
            img.save(thumb_io, 'JPEG', quality=85)
        elif img.mode in ["RGBA", "P"]:
            img = img.convert("RGB")
            img.save(thumb_io, 'JPEG', quality=85)

        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(_("Məhsul Şəkili"), upload_to='products/images/')
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = _("Məhsul Şəkili")
        verbose_name_plural = _("Məhsul Şəkilləri")



class ProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)
    field = models.CharField(_("Xüsusiyyət"), max_length=100)
    content = models.TextField(_("Xüsusiyyət Məzmunu"), null=True, blank=True, max_length=250)

    class Meta:
        verbose_name = _("Məhsul Xüsusiyyətləri")
        verbose_name_plural = _("Məhsul Xüsusiyyətləri")

    def __str__(self):
        return self.field
