from django.urls import path
from .views import HomeView, ProjectDetail, AddProjectView, AddTaskView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('project/<str:slug>', ProjectDetail.as_view(), name="project-detail"),
    path('add-project', views.AddProjectView.as_view(), name="add-project"),
    path('add-task', views.AddTaskView.as_view(), name="add-task"),

]
