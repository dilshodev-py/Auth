from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView

from apps.forms import RegisterForm, ProfileForm
from apps.models import User


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/home.html'


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'apps/profile.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        print(data)

    def form_invalid(self, form):
        data = form.errors
        print(data)


class RegisterFormView(FormView):
    template_name = 'apps/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')
