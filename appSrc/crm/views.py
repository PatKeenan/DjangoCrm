from django.shortcuts import render, redirect
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


@login_required
def crmView(request):
    if request.method == "GET":
        try:
            people = Person.objects.filter(
                author=request.user).order_by('last_name')
            context = {
                "people":people
            }
            return render(request, 'crm/crm_home.html', context)
        except:
            return render(request, 'crm/crm_home.html', {})

def addPerson(request):
    if request.method == "GET":
        form = PersonForm()
        context = {
            "form":form
        }
        return render(request, 'crm/add_person.html', context)
    
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('crm')
        else:
            form = PersonForm()
            context = {}
            return render(request, 'crm/add_person.html', context)


