from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Project(models.Model):
    author = models.ForeignKey(User, verbose_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    project_image = models.CharField(max_length=300)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    project_description = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"slug": self.slug})
    
    

class Task(models.Model):
    assigned_project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE, related_name="assigned_project")
    task = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
    
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"slug": self.assigned_project.slug})
    
