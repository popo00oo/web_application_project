from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Form for user registration
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Form for user login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

