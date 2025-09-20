from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import RegisterForm, RegisterUpdateForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = 'posts:index'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = RegisterUpdateForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
