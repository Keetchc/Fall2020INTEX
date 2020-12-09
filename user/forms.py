from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ApplicantForm(ModelForm) :
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['user']

class SkillsForm(ModelForm):
    class Meta:
        model= ApplicantSkills
        fields = '__all__'