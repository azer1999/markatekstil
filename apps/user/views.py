from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator

# Create your views here.
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

# Create your views here.
from ..base_user.models import MyUser
from core.tools import send_mail


class SignUpView(View):
    form_class = UserRegisterForm
    template_name = 'Auth/register.html'

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.add_message(request, messages.INFO, _("Siz uğurla qeydiyyatdan keçdiniz."
                                                           "Zəhmət olmasa e-poçt ünvanınızı təsdiqləyin"))
            send_mail(
                current_site=get_current_site(request),
                subject=_("Hesab Təsdiqləməsı"),
                user=user,
                to_email=user_form.cleaned_data.get('email'),
                template='account_activation.html'
            )

        return render(request, self.template_name, {'form': user_form})

    def get(self, request):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'Auth/login.html'

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('core:index'))
        else:
            return render(request, self.template_name,
                          {'login_error': _("İstifadəçi adı və yə şifrə düzgün qeyd olunmayıb")})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('core:index')


class ProfileView(TemplateView):
    template_name = 'profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = MyUser._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, _("Qeydiyyat uğurla tamalandı"))
        return redirect(reverse_lazy('core:login'))
    else:
        return redirect(reverse_lazy('core:index'))
