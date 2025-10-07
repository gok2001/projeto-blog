from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m',
        blank=True, null=True
    )
    bio = models.TextField(blank=True)
