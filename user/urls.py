from django.urls import path
from .views import profilePageView

urlpatterns = [
    path('', profilePageView, name='profile'),
]
