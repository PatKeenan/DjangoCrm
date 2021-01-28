from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .forms import *

# Create your views here.

class AddProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/add_project.html'
    form_class = ProjectForm

@login_required
def addProject(request):
    if request.method == "POST":
        user = request.user
        if request.user.is_authenticated:
            form = ProjectForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.date_created = datetime.datetime.now()
            
                instance.save()
                return redirect('/')
    if request.method == "GET":
        if request.user.is_authenticated:
            context = {
                "form" : ProjectForm
            }
            return render(request, 'projects/add_project.html', context)

class AddTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'projects/add_task.html'
    form_class = TaskForm


@login_required
def dashboardView(request):
    if request.method == "GET":
        projects = Project.objects.filter(author=request.user)
        if len(projects) <= 0:
            message = "Welcome to your dashboard, begin by adding a project above."
            context = {
                "message":message
            }
            return render(request, "projects/index.html", context)
        else:
            backup_image = "https://osbornegroupcre.com/wp-content/uploads/2016/02/missing-image-640x360.png"
            context = {
                "projects": projects,
                "backup": backup_image
            }
            return render(request, "projects/index.html", context)
    else:
        return redirect('accounts/login/')

@login_required
def projectDetail(request, slug):
    if request.method == "GET":
        try: 
            projects = Project.objects.get(author=request.user, slug = slug)
            context = {
                "project": projects,
            }
            return render(request, 'projects/project_detail.html', context)
        except:
            return render(request, 'projects/nothing_to_see.html', {})
            
