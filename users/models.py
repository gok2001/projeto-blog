from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(r'^[a-zA-Z0-9]+$')
        ],
    )
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m',
        blank=True, null=True
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
