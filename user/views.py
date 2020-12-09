from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import ApplicantForm, SkillsForm

# Create your views here.

@login_required(login_url='login')
def profilePageView(request) :
    user = request.user
    form = ApplicantForm(instance=user)
    
    if request.method == 'POST' :
        form = User1Form(request.POST, instance=user)
        if form.is_valid() :
            form.save()



    context = {
        'form' : form
    }
    
    

    return render(request, 'user/profile.html', context)
#This portion allows the user to view his/her skills
def listSkills(request):
    skills = ApplicantSkills.objects.filter(user_id = request.user.applicant)
    return render(request, 'homepages/listskills.html', {'skills':skills})


#This portion allows the user to select skills
#def deleteSkills(request, pk):
 #   skill = ApplicantSkills.objects.get(id=pk)
  # context={
   #     'skill':skill
   # }
    #return render(request, 'homepages/deleteskills.html', context)


def successdelete(request):
    if request.method == "POST":
        skill = request.POST.get('skill_id')
        skill.delete()
        return redirect('profile')

def deleteSkills(request, pk):
    skill = ApplicantSkills.objects.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect('profile')
    context={
    'skill':skill
    }
    return render(request, 'homepages/deleteskills.html', context)

