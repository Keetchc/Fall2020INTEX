from django.urls import path
from .views import jobPageView, jobListPageView

urlpatterns = [
    path('job/', jobPageView, name='job'),
    path('', jobListPageView, name='joblist'),
]
