from django.shortcuts import render
from django.http import request

# Create your views here.

def indexPageView(request) :
    return('IndexPageView')

def aboutPageView(request) :
    return('AboutPageView')
    