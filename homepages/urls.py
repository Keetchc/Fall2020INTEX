from django.urls import path
from .views import indexPageView, aboutPageView, azure_matchbox, azure_matchbox_company

urlpatterns = [
    path('', indexPageView, name='home'),
    path('matchbox/', azure_matchbox, name='matchbox'),
    path('matchboxcompany/', azure_matchbox_company, name='matchboxcompany'),
    path('about/', aboutPageView, name='about')
]
