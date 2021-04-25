from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.
from .forms import UserRegisterForm
from  django.shortcuts import render
from django.views.generic import View


# Create your views here.


class SignUpView(View):

    def post(self, request, *args, **kwargs):
        # user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        #     user = user_form.save()
        #     user.set_password(user.password)
        #     user.save()
        #     profile = profile_form.save(commit=False)
        #     profile.user = user
        #     if 'profile_pic' in request.FILES:
        #         profile.profile_pic = request.FILES['profile_pic']
        #     profile.save()
        #     registered = True
        # else:
        #     print(user_form.errors, profile_form.errors)
        return ''

    def get(self, request):
        return render(request,'auth.html')

