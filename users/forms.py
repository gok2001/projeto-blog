from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        min_length=8,
        required=True,
        help_text='Apenas letras e números, sem espaços.',
        strip=True,
        widget=forms.TextInput(attrs={'class': 'input-base'}),
        error_messages={
            'max_length': 'Nome de usuário muito grande. (máx: 30 caracteres)',
            'min_length': 'Nome de usuário muito pequeno. (mín: 8 caracteres)',
            'required': 'Campo obrigatório!',
            'invalid': 'Digite um nome de usuário válido.',
        },
    )
    email = forms.EmailField(
        required=True,
        help_text='Digite um email válido.',
        widget=forms.EmailInput(attrs={'class': 'input-base'}),
        error_messages={
            'required': 'Campo obrigatório!',
            'invalid': 'Digite um email válido.',
        },
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'input-base'}),
        required=True,
        help_text='- Sua senha não pode ser muito parecida com outra informação pessoal. \
                    \n- Sua senha precisa ter pelo menos 8 caracteres. \
                    \n- Sua senha não pode ser uma senha muito comum. \
                    \n- Sua senha não pode ser inteiramente numérica.',
        strip=False,
    )
    password2 = forms.CharField(
        label='Confirma senha',
        widget=forms.PasswordInput(attrs={'class': 'input-base'}),
        required=True,
        help_text='Digite a mesma senha novamente.',
        strip=False,
    )
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'input-base'}),
        required=False,
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input-base'}),
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'password1',
            'password2', 'avatar', 'bio',
        )

    def clean_username(self):
        model = self.Meta.model
        username = self.cleaned_data.get('username')

        if model.objects.filter(username=username).exists():
            raise forms.ValidationError('Um usuário com este nome já existe.')

        return username

    def clean_email(self):
        model = self.Meta.model
        email = self.cleaned_data.get('email')

        if model.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        user = self.instance

        if password1:
            try:
                password_validation.validate_password(password1, user)
            except forms.ValidationError as errors:
                for error in errors:
                    msg = str(error)

                    if 'too similar' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito parecida com algum dado pessoal.'
                        )
                    elif 'too short' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito curta. (mín: 8 caracteres)'
                        )
                    elif 'common' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito comum.'
                        )
                    elif 'entirely numeric' in msg:
                        self.add_error(
                            'password1',
                            'Senha não pode conter apenas números.'
                        )

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError('Senhas não batem')

        return password2


class EditUserForm(forms.ModelForm):
    username = forms.CharField(
        min_length=8,
        required=False,
        help_text='Apenas letras e números, sem espaços.',
        strip=True,
        widget=forms.TextInput(attrs={'class': 'input-base'}),
        error_messages={
            'max_length': 'Nome de usuário muito grande. (máx: 30 caracteres)',
            'min_length': 'Nome de usuário muito pequeno. (mín: 8 caracteres)',
            'invalid': 'Digite um nome de usuário válido.',
        },
    )
    email = forms.EmailField(
        required=False,
        help_text='Digite um email válido.',
        widget=forms.EmailInput(attrs={'class': 'input-base'}),
        error_messages={
            'invalid': 'Digite um email válido.',
        },
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'input-base'}),
        required=False,
        help_text='- Sua senha não pode ser muito parecida com outra informação pessoal. \
                    \n- Sua senha precisa ter pelo menos 8 caracteres. \
                    \n- Sua senha não pode ser uma senha muito comum. \
                    \n- Sua senha não pode ser inteiramente numérica.',
        strip=False,
    )
    password2 = forms.CharField(
        label='Confirma senha',
        widget=forms.PasswordInput(attrs={'class': 'input-base'}),
        required=False,
        help_text='Digite a mesma senha novamente.',
        strip=False,
    )
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'input-base'}),
        required=False,
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input-base'}),
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'password1',
            'password2', 'avatar', 'bio',
        )

    def clean_username(self):
        model = self.Meta.model
        username = self.cleaned_data.get('username')

        if not username:
            return self.instance.username

        if model.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Um usuário com este nome já existe.')

        return username

    def clean_email(self):
        model = self.Meta.model
        email = self.cleaned_data.get('email')

        if not email:
            return self.instance.email

        if model.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este email já está em uso.')

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        user = self.instance

        if password1:
            try:
                password_validation.validate_password(password1, user)
            except forms.ValidationError as errors:
                for error in errors:
                    msg = str(error)

                    if 'too similar' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito parecida com algum dado pessoal.'
                        )
                    elif 'too short' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito curta. (mín: 8 caracteres)'
                        )
                    elif 'common' in msg:
                        self.add_error(
                            'password1',
                            'Senha muito comum.'
                        )
                    elif 'entirely numeric' in msg:
                        self.add_error(
                            'password1',
                            'Senha não pode conter apenas números.'
                        )

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError('Senhas não batem')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)

        avatar = self.cleaned_data.get('avatar')
        if avatar:
            user.avatar = avatar

        bio = self.cleaned_data.get('bio')
        if bio:
            user.bio = bio

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        help_text='Digite seu nome de usuário.',
        strip=True,
        widget=forms.TextInput(attrs={'class': 'input-base'}),
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'input-base'}),
        required=True,
        help_text='Digite sua senha.',
        strip=False,
    )

    error_messages = {
        'invalid_login': 'Usuário ou senha incorretos.'
    }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')

    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if user is None:
    #             raise forms.ValidationError("Usuário ou senha inválidos.")
    #     return cleaned_data
