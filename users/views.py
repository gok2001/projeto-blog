from django.shortcuts import render
from django.views.generic import CreateView

from .forms import RegisterForm


class RegisterView(CreateView):
    model = RegisterForm
    template_name = 'users/register.html'
    success_url = 'users/login.html'
