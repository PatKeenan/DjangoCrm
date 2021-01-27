from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
=======
import datetime
>>>>>>> views

from .forms import *

# Create your views here.


<<<<<<< HEAD
class HomeView(LoginRequiredMixin, ListView):
=======
""" class HomeView(LoginRequiredMixin, ListView):
>>>>>>> views
    model = Project
    template_name = 'projects/index.html'
 """


""" class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project

    def get_queryset(self):
        if request.user == Project.objects.filter(author=self.)
        return Project.objects.filter(author=self.request.user)
        template_name = 'projects/project_detail.html'
 """

class AddProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/add_project.html'
    form_class = ProjectForm

@login_required
def addProject(request):
    if request.method == "POST":
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

<<<<<<< HEAD
""" @login_required
def homeView(request):
    projects = Project.objects.filter(author=request.user)
 """
=======


def homeView(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            projects = Project.objects.filter(author=request.user)

            context = {
                "projects": projects
            }
            return render(request, "projects/index.html", context)
        else:
            return redirect('accounts/login/')


def projectDetail(request, slug):
    
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                project = Project.objects.get(author=request.user, slug = slug)
                context = {
                    "project": project
                }
                return render(request, 'projects/project_detail.html', context)
            except:
                return render(request, "projects/nothing_to_see.html",{})
        else:
            return redirect('accounts/login/')

>>>>>>> views
