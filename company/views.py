from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Job

# Create your views here.


def jobListPageView(request) :
    data = Job.objects.all()
    context = {
        "jobs": data
    }
    return render(request, 'company/joblist.html', context)