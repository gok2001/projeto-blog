from django import forms
from django.core.exceptions import ValidationError

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            'title', 'content', 'summary',
            'category', 'tags', 'image',
        )


class CommentForm(forms.ModelForm):
    parent_id = forms.IntegerField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = models.Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'maxlength': 500,
                'rows': 5,
                'placeholder': 'Escreva seu comentário aqui...',
                'class': 'input-base',
            }),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text', '') or ''
        text = text.strip()

        if len(text) < 3:
            raise ValidationError(
                'Escreva uma mensagem um pouco mais longa.',
                code='min_length',
            )

        return text
