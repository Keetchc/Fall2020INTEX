from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Job, Company
from user.models import Applicant, Skill, Job_Skills, Skill
from django.contrib.auth.models import User

# Create your views here.


def jobListPageView(request) :
    data = Job.objects.all()
    context = {
        "jobs": data
    }
    return render(request, 'company/joblist.html', context)


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
            company_id = Company.objects.get(company_name = request.POST.get('company_id')), 
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
                
                
        return render(request, 'homepages/companyhome.html')   
