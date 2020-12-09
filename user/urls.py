from django.urls import path
from .views import profilePageView, listSkills, deleteSkills, successdelete

urlpatterns = [
    path('', profilePageView, name='profile'),
    path('listskills/', listSkills, name='listskills'),
    path('deleteskills/<str:pk>/', deleteSkills, name='deleteskills'),
    path('sucessdelete/',successdelete, name="successdelete")
]
