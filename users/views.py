from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .forms import EditUserForm, ProfileForm, RegisterForm


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        user_form, profile_form = self.get_forms()

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form, profile_form = self.get_forms(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Conta criada com sucesso!')

            return redirect(reverse_lazy('users:login'))

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def get_forms(self, data=None, files=None):
        user_form = RegisterForm(data)
        profile_form = ProfileForm(data, files)

        return (user_form, profile_form)


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Bem-vindo, {form.get_user()}!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:index')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'users/edit_profile.html'

    def get(self, request, *args, **kwargs):
        user_form, profile_form = self.get_forms(
            user_instance=request.user,
            profile_instance=request.user.profile
        )

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form, profile_form = self.get_forms(
            data=request.POST,
            files=request.FILES,
            user_instance=request.user,
            profile_instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            if user_form.cleaned_data.get('password1'):
                update_session_auth_hash(request, user)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Perfil atualizado com sucesso!')

            return redirect(reverse_lazy('users:profile'))

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def get_forms(self, data=None, files=None, user_instance=None, profile_instance=None):
        user_form = EditUserForm(data, instance=user_instance)
        profile_form = ProfileForm(data, files, instance=profile_instance)

        return (user_form, profile_form)
