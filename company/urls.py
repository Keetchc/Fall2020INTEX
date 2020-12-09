from django.urls import path
from .views import jobListPageView, viewApplicantsPageView, postAJobPageView, storeAJobPageView

urlpatterns = [
    path('', jobListPageView, name='joblist'),
    path('viewapplicants/', viewApplicantsPageView, name='applicantlist'),
    path('postajob/', postAJobPageView, name='postajob'),
    path('storeajob/', storeAJobPageView, name='storeajob')

]
