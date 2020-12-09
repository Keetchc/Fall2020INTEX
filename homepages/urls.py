from django.urls import path
from .views import indexPageView, aboutPageView, azure_matchbox, azure_matchbox_company, employerPageView, employerAboutPageView

urlpatterns = [
    path('', indexPageView, name='home'),
    path('employerabout/', employerAboutPageView, name='empabout'),
    path('employerhome/', employerPageView, name='emphome'),
    path('matchbox/', azure_matchbox, name='matchbox'),
    path('matchboxcompany/', azure_matchbox_company, name='matchboxcompany'),
    path('about/', aboutPageView, name='about')
]
