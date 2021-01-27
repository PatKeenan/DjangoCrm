from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['title','author', 'project_image', 'project_description',]


admin.site.register(Task)
