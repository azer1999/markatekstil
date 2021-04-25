from django.views.generic import TemplateView
from apps.product.models import Product, Category
from core.models import Slider, About, Partner, Advantage, FAQ

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['slider'] = Slider.objects.all()
        context['categories_list'] = Category.objects.filter(parent=None).all()
        context['partners'] = Partner.objects.all()[:10]
        context['advantages'] = Advantage.objects.all()
        return context
