from django.forms import ModelForm

from core.models import ContactFeedback, Subscribe


class ContactFeedbackForm(ModelForm):
    class Meta:
        model = ContactFeedback
        fields = ('name','email','message')

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)