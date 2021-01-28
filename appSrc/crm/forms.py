from django import forms
from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2 col-md-6', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2 col-md-6', 'placeholder': 'Smith'}),
            'email': forms.TextInput(attrs={'class': 'form-control my-2', 'type': 'email', 'placeholder': "example@gmail.com"}),
            'phone': forms.TextInput(attrs={'class': 'form-control my-2', 'type': 'tel', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}', 'placeholder':"555-555-1234"}),
            'relations': forms.Select(attrs={'class': 'form-select my-2'}),
            'level': forms.Select(attrs={'class': 'form-select my-2'}),
            'properties': forms.SelectMultiple(attrs={'class': 'form-select my-2'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control my-2', 'type': 'url', 'placeholder': 'https://www.twitter.com/profile'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control my-2', 'type': 'url', 'placeholder': 'https://www.facebook.com/profile'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control my-2', 'type': 'url', 'placeholder': 'https://www.instagram.com/profile'})
   
        }


