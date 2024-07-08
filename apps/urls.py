from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import HomeView, RegisterFormView, ProfileUpdateView

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('login', LoginView.as_view(template_name = 'apps/login.html') , name='login'),
    path('logout', LogoutView.as_view(template_name = 'apps/login.html') , name='logout'),
    path('register', RegisterFormView.as_view() , name='register'),
    path('profile', ProfileUpdateView.as_view() , name='profile'),
]

