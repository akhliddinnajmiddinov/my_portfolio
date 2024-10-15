from django.contrib import admin
from .models import HashtagForProject, Project

# Register your models here.
admin.site.register(HashtagForProject)
admin.site.register(Project)