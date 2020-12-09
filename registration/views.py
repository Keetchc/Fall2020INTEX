from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm, CreateEmployerForm
from user.models import Applicant
from company.models import Company
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

#This portion allows the user to select whether they are an employer or applicant.

def employerOrApplicantPageView(request) :
    return render (request, 'registration/applicantoremployer.html')


#This section is for the Applicant form

#This allow the Applicant to register
@unauthenticated_user
def registerPageView(request) :

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            group = Group.objects.get(name='Applicant')
            user.groups.add(group)
            Applicant.objects.create(
                user=user,
                first_name= first_name,
                last_name = last_name,
                email = email,
                phone_number = phone_number
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


#This allows the Applicant to login
@unauthenticated_user
def loginPageView(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('emporapp') #EmployerOrApplicantPage

#Testing
@login_required(login_url='login')
@allowed_users(allowed_roles=['Applicant'])
def gettingStartedPageView(request) :
    orders = request.user.applicant.email
    print('Orders:', orders)
    context = {'orders':orders}
    return render(request, 'registration/gettingstarted.html', context)

#This section is for the Employer

#This allows the Employer to reigster
@unauthenticated_user
def registerEmployerPageView(request) :

    form = CreateEmployerForm()

    if request.method == 'POST':
        form = CreateEmployerForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            city = form.cleaned_data.get('city')
            address = form.cleaned_data.get('address')
            zip_code = form.cleaned_data.get('zip_code')
            state = form.cleaned_data.get('state')
            country = form.cleaned_data.get('country')
            group = Group.objects.get(name='Employer')
            user.groups.add(group)
            Company.objects.create(
                user=user,
                company_name=username,
                city=city,
                address=address,
                zip_code=zip_code,
                state=state,
                country=country,

                

            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('emplogin') #redirect to employerlogin page

    context = {'form':form}
    return render(request, 'registration/employerregister.html', context)

@unauthenticated_user
def employerLoginPageView(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('emphome')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'registration/employerlogin.html', context)