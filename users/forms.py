from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
    )

    email = forms.EmailField()

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
