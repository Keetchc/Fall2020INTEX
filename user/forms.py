from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class User1Form(ModelForm) :
    class Meta:
        model = User1
        fields = '__all__'
        exclude = ['user']