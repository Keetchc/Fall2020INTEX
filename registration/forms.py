from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    phone_number = forms.IntegerField()
    

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','phone_number']

class CreateEmployerForm(UserCreationForm) :
    city = forms.CharField()
    address = forms.CharField()
    zip_code = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    
    

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'city', 'address', 'zip_code', 'state', 'country']
