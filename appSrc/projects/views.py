from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/index.html'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    
    
class AddProjectView(CreateView):
    model = Project
    template_name = 'projects/add_project.html'
    form_class = ProjectForm


class AddTaskView(CreateView):
    model = Task
    template_name = 'projects/add_task.html'
    form_class = TaskForm

""" @login_required
def homeView(request):
    projects = Project.objects.filter(author=request.user)
 """