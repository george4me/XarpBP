from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInfo



class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=False)
    #phone=forms.CharField(max_length=50, required=False)
    #gender=forms.CharField(max_length=50, required=False)
    username=forms.CharField(max_length=50, required=True)
    email=forms.CharField(max_length=50)
    password1=forms.CharField(max_length=50)
    password2=forms.CharField(max_length=50)


    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')