from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

def jobPageView(request) :
    return render(request, 'company/job.html')

def jobListPageView(request) :
   return render(request, 'company/joblist.html')