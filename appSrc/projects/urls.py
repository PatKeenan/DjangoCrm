from django.urls import path
from .views import AddTaskView, dashboardView, projectDetail, addProject
from . import views

urlpatterns = [
    path('dashboard/', dashboardView, name="dahsboard-view"),
    path('project/<slug:slug>', projectDetail, name="project-detail"),
    path('add-project/', addProject, name="add-project"),
    path('add-task/', views.AddTaskView.as_view(), name="add-task"),

]
