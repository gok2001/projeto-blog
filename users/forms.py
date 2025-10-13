from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        min_length=8,
        required=True,
        help_text='Apenas letras e números, sem espaços',
        strip=True,
        error_messages={
            'max_length': 'Nome de usuário muito grande',
            'min_length': 'Nome de usuário muito pequeno',
            'required': 'Campo obrigatório',
        }
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'password1', 'password2'
        )

    def clean_email(self):
        model = self.Meta.model
        email = self.cleaned_data.get('email')

        if model.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')

        return email


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
        model = get_user_model()
        fields = ('username', 'email', 'avatar', 'bio',)
        widgets = {
            'bio': forms.Textarea(),
        }

    def clean_email(self):
        model = self.Meta.model
        email = self.cleaned_data.get('email')

        if model.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
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
        pw = self.cleaned_data.get('password1', '')

        if pw:
            user.set_password(pw)
        if commit:
            user.save()

        return user
