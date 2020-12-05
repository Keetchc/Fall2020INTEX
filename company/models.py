from django.db import models
from datetime import datetime

# Create your models here.

class Company(models.Model) :
    company_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)

    def __str__(self) :
        return (self.company_name)