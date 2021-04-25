from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.base_user.models import MyUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'first_name',)
