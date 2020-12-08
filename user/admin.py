from django.contrib import admin
from .models import User1, UserSkills, Job_Skills, Skill, AppliesFor
# Register your models here.

admin.site.register(User1)
admin.site.register(UserSkills)
admin.site.register(Job_Skills)
admin.site.register(Skill)
admin.site.register(AppliesFor)
