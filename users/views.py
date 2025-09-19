from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = 'posts:index'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
