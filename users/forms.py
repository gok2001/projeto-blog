from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio',)
        widgets = {
            'bio': forms.Textarea(),
        }


class EditUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput,
        required=False
    )

    password2 = forms.CharField(
        label='Confirme a nova senha',
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este email já está em uso.')

        return email

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')

        if pw1 or pw2:
            if pw1 != pw2:
                raise forms.ValidationError('As senhas não coincidem.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        pw = self.cleaned_data.get('password1')

        if pw:
            user.set_password(pw)
        if commit:
            user.save()

        return user
