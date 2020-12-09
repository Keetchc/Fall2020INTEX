from django.contrib import admin
from .models import Applicant, ApplicantSkills, Job_Skills, Skill, AppliesFor
# Register your models here.

admin.site.register(Applicant)
admin.site.register(ApplicantSkills)
admin.site.register(Job_Skills)
admin.site.register(Skill)
admin.site.register(AppliesFor)
