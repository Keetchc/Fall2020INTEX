from django.urls import path
from .views import jobListPageView, viewApplicantsPageView, postAJobPageView, storeAJobPageView, jobPageView, companyJobListPageView, companyJobPageView

urlpatterns = [
    path('', jobListPageView, name='joblist'),
    path('job/', jobPageView, name='job'),
    path('companyjob/', companyJobPageView, name='companyjob'),
    path('companyjobs/', companyJobListPageView, name='companyjoblist' ),
    path('viewapplicants/', viewApplicantsPageView, name='applicantlist'),
    path('postajob/', postAJobPageView, name='postajob'),
    path('storeajob/', storeAJobPageView, name='storeajob')

]
