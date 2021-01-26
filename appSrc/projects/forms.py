from django import forms
from .models import * 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =  ('title', 'project_image','project_description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'project_image': forms.TextInput(attrs={'class': 'form-control'}),
            'project_description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("assigned_project","task",'status')

        widgets = {
            'assigned_project': forms.Select(attrs={'class': 'form-select' ,'placeholder':'select project'}),
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter task here'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
