from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from apps.product.models import Category
from core.forms import ContactFeedbackForm, SubscribeForm
from core.models import Slider, Partner, Advantage, ContactInfo, About, FAQ, Delivery, PayMethods
from django.utils.translation import ugettext_lazy as _


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        print(get_current_site(self.request), "+++++")

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['slider'] = Slider.on_site.all()
        context['categories_list'] = Category.objects.filter(parent=None, site=settings.SITE_ID).all()
        context['partners'] = Partner.objects.all()[:10]
        context['advantages'] = Advantage.objects.all()
        return context


class IndexSetPageView(TemplateView):
    template_name = 'index-set.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['sites'] = Site.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['about'] = About.objects.last()

        return context


class FaqView(TemplateView):
    template_name = 'faq.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['faq'] = FAQ.objects.all()

        return context


class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactFeedbackForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 _("Sualınız qeydə alındı.Sizinlə yaxın müddətdə əlaqə qurulacaq"))
            return redirect(reverse('core:index', args=(get_current_site(request).name,)))

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = self.form_class
        context['contact'] = ContactInfo.objects.last()
        return render(request, self.template_name, context)


class SubscribeView(View):
    form_class = SubscribeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 _("Siz uğurla xəbərlərə abunə oldunuz."))
        else:
            print(form.errors)
            messages.add_message(request, messages.INFO,
                                 _("Xəta baç verdi"))
        return redirect(reverse('core:index', args=(get_current_site(request).name,)))


class DeliveryView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page'] = Delivery.objects.last()

        return context


class PayMethodsView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page'] = PayMethods.objects.last()

        return context


def set_site(request, id):
    try:
        current_site = Site.objects.get(id=id)
    except Site.DoesNotExist:
        current_site = Site.objects.get(id=settings.SITE_ID)

    request.current_site = current_site
    settings.SITE_ID = current_site.id

    return redirect('core:index')
