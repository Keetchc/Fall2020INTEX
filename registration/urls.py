from django.urls import path
from .views import employerOrApplicantPageView, employerLoginPageView, registerEmployerPageView, loginPageView, logoutUser, registerPageView, gettingStartedPageView

urlpatterns = [
    #this section is for employers
    path('', employerOrApplicantPageView, name='emporapp'),
    path('employerlogin/', employerLoginPageView, name='emplogin'),
    path('employerregister/', registerEmployerPageView, name='empregister'),
    #this section is for applicants
    path('login/', loginPageView, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('register/', registerPageView, name='register'),
    path('gettingstarted/', gettingStartedPageView, name='gettingStarted'),
]
