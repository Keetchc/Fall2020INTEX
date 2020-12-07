from django.db import models
from company.models import Job

# Create your models here.

class User(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    jobs_offered = models.IntegerField()

    def __str__(self) :
        return(self.first_name + ' ' + self.last_name)


class Skill(models.Model) :
    skill_name = models.CharField(max_length=30)

    def __str__(self) :
        return(self.skill_name)

class Job_Skills(models.Model) :
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE) #FOREIGN KEY OR ManyToOneField?
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)



    def __str__(self) :
        return(str(self.job_id) + '-' + str(self.skill_id))


class UserSkills(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #FOREIGN KEY OR ManyToOneField?
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_profciency = models.IntegerField()

    def __str__(self) :
        return(str(self.user_id) + '-' + str(self.skill_id))

class AppliesFor(models.Model) :
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE)
    date_applied = models.DateField()

    def __str__ (self) :
        return(str(self.user_id) + '-' + str(self.job_id))


