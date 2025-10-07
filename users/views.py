from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import ProfileForm, RegisterForm, RegisterUpdateForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        user_form = RegisterForm()
        profile_form = ProfileForm()

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect(self.success_url)

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = 'posts:index'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get(self, request, *args, **kwargs):
        user_form = RegisterForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = RegisterForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect(self.success_url)

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )
