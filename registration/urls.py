from django.urls import path
from .views import loginPageView, registerPageView, gettingStartedPageView, logoutUser

urlpatterns = [
    path('', loginPageView, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('register/', registerPageView, name='register'),
    path('gettingstarted/', gettingStartedPageView, name='gettingStarted')
]
