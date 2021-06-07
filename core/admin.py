from django.contrib import admin
from django.contrib.sites.models import Site

from core.models import Partner, Slider, SocialMedia, ContactInfo, About, ContactFeedback, Advantage, Logo, FAQ, \
    Subscribe, SiteImage, Delivery, PayMethods

admin.site.register(Partner)
admin.site.register(Subscribe)
admin.site.register(Logo)
admin.site.register(Slider)
admin.site.register(SocialMedia)
admin.site.register(ContactInfo)
admin.site.register(About)
admin.site.register(ContactFeedback)
admin.site.register(Advantage)
admin.site.register(FAQ)
admin.site.register(Delivery)
admin.site.register(PayMethods)

# Admin
admin.site.unregister(Site)


class SiteImageInline(admin.StackedInline):
    model = SiteImage


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteImageInline]
