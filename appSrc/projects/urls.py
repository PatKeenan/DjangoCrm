from django.urls import path
from .views import AddTaskView, homeView, projectDetail, addProject
from . import views

urlpatterns = [
    path('', homeView, name="home"),
    path('project/<slug:slug>', projectDetail, name="project-detail"),
    path('add-project', addProject, name="add-project"),
    path('add-task', views.AddTaskView.as_view(), name="add-task"),

]
