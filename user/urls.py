from django.urls import path
from .views import profilePageView

urlpatterns = [
    path('profile/', profilePageView, name='profile'),
]
