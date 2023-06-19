from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

from regs.models import Hospital
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def validate_password(self):
        if self.password2 != self.password:
            return ValueError("Password and Confirm Password must be equal")
        return self.password

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'national_id', 'email', 'phone_number', 'password', 'password2']


class LoginForm(AuthenticationForm):
    national_id = forms.CharField(max_length=20)


class ResetPasswordForm(PasswordResetForm):
    national_id = forms.CharField(max_length=40)


class HospitalRegistrationForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = "__all__"
