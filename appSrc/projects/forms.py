from django import forms
from .models import * 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'project_description', 'assigned_folder')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "My Awesome Project"}),
            'project_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "https://source.unsplash.com/random/800x600"}),
            'project_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Describe Your Project"}),
            'assigned_folder': forms.Select(attrs={'class': 'form-select', 'placeholder': 'select folder'})
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
