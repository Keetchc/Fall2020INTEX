from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model) :
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    

    def __str__(self) :
        return (self.company_name)

class Job(models.Model) :
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=50)
    job_description = models.CharField(max_length=1000)
    date_posted = models.DateField()

    def __str__(self) :
        return (self.job_name)

