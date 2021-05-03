from ckeditor.fields import RichTextField
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.db import models
from pytz import unicode
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from pytz import unicode


class SocialMedia(models.Model):
    media_types = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube')
    )
    media = models.CharField(choices=media_types, max_length=55, unique=True)
    url = models.URLField(_("Link"))

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return unicode(f'{self.media}')


class FAQ(models.Model):
    question = models.TextField(_("Sual"))
    answer = models.TextField(_("Cavab"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")

    def __str__(self):
        return unicode(f'{self.id}')


class Logo(models.Model):
    image = models.ImageField(upload_to='logo/images/')
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _("Loqo")
        verbose_name_plural = _("Loqo")

    def __str__(self):
        return unicode(f'{self.id}')


class About(models.Model):
    content = RichTextField(_("Mətn"))

    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")

    def __str__(self):
        return unicode(f'{self.id}')


class Slider(models.Model):
    image = models.ImageField(upload_to='core/slider/images')
    text = models.CharField(_("Mətn"), max_length=55)
    button_url = models.URLField()
    button_text = models.CharField(_("Mətn"), max_length=55)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = _("Slayder")
        verbose_name_plural = _("Slayderlər")

    def __str__(self):
        return f'{self.id}'


class Advantage(models.Model):
    image = models.ImageField(upload_to='advantages/images')
    title = models.CharField(_("Başlıq"), max_length=100)
    text = models.CharField(_("Mətn"), max_length=100)

    class Meta:
        verbose_name = _("Üstünlük")
        verbose_name_plural = _("Üstünlüklər")

    def __str__(self):
        return f'{self.id}'


class Partner(models.Model):
    image = models.ImageField(_("Şəkil"), upload_to='products/images/')
    name = models.CharField(_("Adı"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tərəfdaş")
        verbose_name_plural = _("Tərəfdaşlar")


class ContactInfo(models.Model):
    phone = models.CharField(_("Telefon"), max_length=55)
    email = models.CharField(_("E-poçt"), max_length=55)
    address = models.CharField(_("Adres"), max_length=100)

    text = models.CharField(_("Mətn"), max_length=150)

    class Meta:
        verbose_name = _("Əlaqə")
        verbose_name_plural = _("Əlaqə")

    def __str__(self):
        return unicode(f'{self.id}')


class ContactFeedback(models.Model):
    name = models.CharField(_("Adı"), max_length=55)
    email = models.EmailField(_("E-poçt"))
    message = models.TextField(_("Mesaj"))
    subject = models.CharField(_("Mövzu"), max_length=55)
    _("Mesaj")

    class Meta:
        verbose_name = _("Əlaqə muraciətləri")
        verbose_name_plural = _("Əlaqə muraciətləri")

    def __str__(self):
        return unicode(self.id)


class Subscribe(models.Model):
    email = models.EmailField(_("E-poçt"), unique=True)

    class Meta:
        verbose_name = _("Abunələr")
        verbose_name_plural = _("Abunələr")

    def __str__(self):
        return unicode(self.email)


class SiteImage(models.Model):
    image = models.ImageField(upload_to='site/images/')
    site = models.OneToOneField(Site,on_delete=models.CASCADE,related_name='site_images')
    def __str__(self):
        return f'{self.id}'
