from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('crm/', crmView, name="crm"),
    path('crm/add-person', addPerson, name="add-person")
]
