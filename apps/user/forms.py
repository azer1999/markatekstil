from django import forms

from apps.base_user.models import MyUser
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("İki parol sahəsi uyğun gəlmədi."),
    }
    password1 = forms.CharField(label=_("Şifrə"),
                                widget=forms.PasswordInput(attrs={'col_md': 6}))
    password2 = forms.CharField(label=_("Şifrə Təsdiqi"),
                                widget=forms.PasswordInput(attrs={'col_md': 6}))

    class Meta:
        model = MyUser
        fields = ("email", "username", "first_name", "last_name",)
        widgets = {
            'username': forms.TextInput(attrs={'col_md': 12}),
            'email': forms.EmailInput(attrs={'col_md': 12}),
            'first_name': forms.TextInput(attrs={'col_md': 6}),
            'last_name': forms.TextInput(attrs={'col_md': 6}),
            'password1': forms.TextInput(),
            'password2': forms.TextInput(attrs={'col_md': 6}),
        }

    field_order = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
