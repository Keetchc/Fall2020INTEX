from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.


def profilePageView(request) :
    return render(request, 'user/profile.html')