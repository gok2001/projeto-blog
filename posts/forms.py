from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('text',)
