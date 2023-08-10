from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import GeekUser


class GeekUserCreationForm(UserCreationForm):
    class Meta:
        model = GeekUser
        fields = ("email",)


class GeekUserChangeForm(UserChangeForm):
    class Meta:
        model = GeekUser
        fields = ("email",)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput)

    class Meta:
        model = GeekUser
        fields = [ "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd["password2"]