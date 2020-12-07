from django.urls import path
from .views import loginPageView, registerPageView, gettingStartedPageView

urlpatterns = [
    path('', loginPageView, name='login'),
    path('register/', registerPageView, name='register'),
    path('gettingstarted/', gettingStartedPageView, name='gettingStarted')
]
