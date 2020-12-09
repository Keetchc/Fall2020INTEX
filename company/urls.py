from django.urls import path
from .views import jobListPageView, viewApplicantsPageView, postAJobPageView, storeAJobPageView, jobPageView, companyJobListPageView, companyJobPageView, employerProfilePageView, applicantPageView

urlpatterns = [
    path('', jobListPageView, name='joblist'),
    path('job/', jobPageView, name='job'),
    path('companyjob/', companyJobPageView, name='companyjob'),
    path('applicant/', applicantPageView, name='applicant'),
    path('employerprofile/', employerProfilePageView, name='empprofile'),
    path('companyjobs/', companyJobListPageView, name='companyjoblist' ),
    path('viewapplicants/', viewApplicantsPageView, name='applicantlist'),
    path('postajob/', postAJobPageView, name='postajob'),
    path('storeajob/', storeAJobPageView, name='storeajob')

]
