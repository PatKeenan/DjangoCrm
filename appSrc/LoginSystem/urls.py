from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', mainView, name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view() , name="logout"),
    path('logout-confirmation/', logoutView, name='logut-confirmation'),
    path('register/', registerView,name="register"),
    path('profile/', profileView, name="profile-page"),
    path('profile-edit/', editProfileView, name="profile-edit")
]
