from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
  pass

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','email']
