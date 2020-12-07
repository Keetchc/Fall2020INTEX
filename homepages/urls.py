from django.urls import path
from .views import indexPageView, aboutPageView, azure_matchbox

urlpatterns = [
    path('', indexPageView, name='home'),
    path('matchbox/', azure_matchbox, name='matchbox'),
    path('about/', aboutPageView, name='about')
]
