from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']