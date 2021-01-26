from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *

# Create your views here.
class HomeView(ListView):
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
