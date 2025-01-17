from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# - Create/Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']


# - Authentication of user
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
