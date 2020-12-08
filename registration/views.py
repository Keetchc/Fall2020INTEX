from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from user.models import User1

# Create your views here.
def registerPageView(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                User1.objects.create(
                    user=user,
                )
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'registration/register.html', context)


def loginPageView(request) :
    if request.user.is_authenticated:
        return redirect('home')
    else:
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
    return redirect('login')

@login_required(login_url='login')
def gettingStartedPageView(request) :
    orders = request.user.user1.email
    print('Orders:', orders)
    context = {'orders':orders}
    return render(request, 'registration/gettingstarted.html', context)