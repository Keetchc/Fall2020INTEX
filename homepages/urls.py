from django.urls import path
from .views import indexPageView, aboutPageView

urlpatterns = [
    path('', indexPageView, name='home'),
    path('about/', aboutPageView, name='about')
]
