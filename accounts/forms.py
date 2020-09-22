from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('username', 'votingpoint')

class LoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ('username', 'password')