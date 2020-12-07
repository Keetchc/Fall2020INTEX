from django.db import models
from company.models import Job

# Create your models here.

class User(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self) :
        return(self.first_name + ' ' + self.last_name)


class Skill(models.Model) :
    skill_name = models.CharField(max_length=30)

    def __str__(self) :
        return(self.skill_name)

class Job_Skills(models.Model) :
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE) #FOREIGN KEY OR ManyToOneField?
    skill_id = models.ManyToManyField(Skill)



    def __str__(self) :
        return(self.job_id + '-' + self.skill_id)


class UserSkills(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING) #FOREIGN KEY OR ManyToOneField?
    skill_id = models.ManyToManyField(Skill)
    skill_profciency = models.IntegerField()

    def __str__(self) :
        return(self.user_id + '-' + self.skill_id)

class AppliesFor(models.Model) :
    user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    job_id = models.OneToOneField(Job, on_delete=models.DO_NOTHING)
    date_applied = models.DateField()

    def __str__ (self) :
        return(self.user_id + self.job_id)


