from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .forms import EditUserForm, RegisterUserForm, LoginForm


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        user_form = self.get_forms()

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = self.get_forms(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Conta criada com sucesso!')

            return redirect(reverse_lazy('users:login'))
        else:
            messages.error(
                request,
                'Por favor, corrija os erros no formulário.'
            )

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
            }
        )

    def get_forms(self, data=None, files=None):
        user_form = RegisterUserForm(data, files)

        return user_form


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def form_valid(self, form):
        messages.success(self.request, f'Bem-vindo, {form.get_user()}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login inválido!')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('posts:index')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'users/edit_profile.html'

    def get(self, request, *args, **kwargs):
        user_form = self.get_forms(
            instance=request.user,
        )

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user_form = self.get_forms(
            data=request.POST,
            files=request.FILES,
            instance=request.user,
        )

        if user_form.is_valid():
            user_form.save()

            if user_form.cleaned_data.get('password1'):
                update_session_auth_hash(request)

            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect(reverse_lazy('users:profile'))
        else:
            messages.error(request, 'Não foi possível atualizar os dados.')

        return render(
            request,
            self.template_name,
            {
                'user_form': user_form,
            }
        )

    def get_forms(self, data=None, files=None, instance=None):
        initial = {
            'username': instance.username,
            'email': instance.email,
            'bio': instance.bio,
        }
        user_form = EditUserForm(data=data, files=files, instance=instance, initial=initial)

        return user_form
