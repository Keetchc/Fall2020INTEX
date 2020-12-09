from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Job, Company
from user.models import Applicant, Skill, Job_Skills, Skill
from .models import *

from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import EmployerForm


# Create your views here.

@login_required(login_url='emplogin')
def employerProfilePageView(request) :
    user = request.user.company
    form = EmployerForm(instance=user)
    
    if request.method == 'POST' :
        form = EmployerForm(request.POST, instance=company)
        if form.is_valid() :
            form.save()



    context = {
        'form' : form
    }
    
    

    return render(request, 'company/companyprofile.html', context)

def jobListPageView(request) :
    data = Job.objects.all()
    context = {
        "jobs": data
    }
    return render(request, 'company/joblist.html', context)

def companyJobListPageView(request) :
    data = Job.objects.filter(company_id = request.user.company)

    context = {
        "jobs" : data
    }

    return render(request, 'company/companyjobs.html', context)

def companyJobPageView(request) :
    if request.method == 'POST' :
        applicable_job_name = request.POST.get('job_id')
        


        data = Job.objects.filter(id= applicable_job_name)

        context = {
            "job" : data,
        }

    return render (request, 'company/companyjob.html', context)

def applicantPageView(request) :
    if request.method == 'POST' :
        applicable_applicant = request.POST.get('applicant_email')
        


        data = Applicant.objects.filter(email= applicable_applicant)

        context = {
            "applicant" : data,
        }

    return render (request, 'company/applicant.html', context)

def jobPageView(request) :
    if request.method == 'POST' :
        applicable_job_id = request.POST.get('job_id')
        


        data = Job.objects.filter(id = applicable_job_id)

        context = {
            "job" : data
        }

    return render (request, 'company/job.html', context)




def viewApplicantsPageView(request) :
    data = Applicant.objects.all()
    context = {
        "applicants": data
    }

    return render(request, 'company/viewapplicants.html', context)

def postAJobPageView(request) :
    data = Skill.objects.all()
    context = {
        "skills" : data
    }
    return render(request, 'company/postjob.html', context)

def storeAJobPageView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_job = Job(
            company_id = Company.objects.get(id = request.POST.get('company_id')), 
            job_name = request.POST.get('job_name'),
            job_description = request.POST.get('job_description'),
            date_posted = request.POST.get('date_posted'),

        )

        new_job.save()

       
        new_job_skill = Job_Skills(
            job_id = Job.objects.get(id=new_job.id),
            skill_id = Skill.objects.get(skill_name = request.POST.get('skill_name')),
        )
        new_job_skill.save()
                
    data = Job.objects.all()

    context = {
        "jobs" : data
    }
                
    return render(request, 'company/companyjobs.html', context)   
