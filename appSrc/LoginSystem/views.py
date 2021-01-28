from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def mainView(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        else:
            return redirect("/login/")

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'LoginSystem/login.html', context)


def logoutView(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/logout/")
        context = {}
        return render(request, 'LoginSystem/logout.html', context)


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm(request.POST)
            context = {
                "form":form
            }
            return render(request, 'LoginSystem/register.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request, 'LoginSystem/register.html', context)

def profileView(request):
    context = {}
    return render(request, 'LoginSystem/profile_home.html', context)

def editProfileView(request):
    context = {}
    return render(request, 'LoginSystem/edit_profile.html', context)

