from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'national_id', 'email', 'phone_number', 'password']

class LoginForm(AuthenticationForm):
    national_id = forms.CharField(max_length=20)

class ResetPasswordForm(PasswordResetForm):
    national_id = forms.CharField(max_length=40)