from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse


class DynamicSiteDomainMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.domain = None
        self.view_name = None
        # One-time configuration and initialization.

    def process_view(self, request, view_func, view_args, view_kwargs):
        self.domain = view_kwargs.get('domain')
        try:
            current_site = Site.objects.get(name=self.domain)
        except Site.DoesNotExist:
            print('not exist')
            current_site = Site.objects.get(id=settings.DEFAULT_SITE_ID)
        request.current_site = current_site
        settings.SITE_ID = current_site.id

    def __call__(self, request):
        response = self.get_response(request)
        print(self.domain, 'domain')

        return response
