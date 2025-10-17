from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def post_count(self):
        return self.post_set.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    def post_count(self):
        return self.post_set.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    content = models.TextField()
    summary = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(
        upload_to='post_images/%Y/%m',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text[:20]

    def clean(self):
        errors = {}
        field_text = (self.text or '').strip()

        if len(field_text) > 500:
            errors['text'] = _(
                'Texto atingiu o limite de caracteres (%(max_length)d).'
            ) % {'max_length': 500}

        if self.parent and self.parent.pk == self.pk:
            errors['parent'] = _(
                'Um comentário não pode ser pai de si mesmo.'
            )

        if self.parent and self.parent.post_id != self.post_id:
            errors['parent'] = _(
                'O comentário pai deve pertencer ao mesmo post.'
            )

        if errors:
            raise ValidationError(errors)
