from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class EmployerForm(ModelForm) :

    class Meta :
        model = Company
        fields = '__all__'
        exclude = ['user']