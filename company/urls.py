from django.urls import path
from .views import jobListPageView

urlpatterns = [
    path('', jobListPageView, name='joblist'),
]
