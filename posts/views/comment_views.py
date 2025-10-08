from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from posts.forms import CommentForm
from posts.models import Post, Comment


class CommentCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/post_detail.html'
    success_message = 'Comentário criado com sucesso.'

    def form_valid(self, form):
        post_id = self.kwargs.get('post_id')
        form.instance.post = get_object_or_404(Post, id=post_id)
        form.instance.author = self.request.user
        parent_id = form.cleaned_data.get('parent_id')

        if parent_id:
            try:
                parent_comment = Comment.objects.get(id=parent_id)
                form.instance.parent = parent_comment
            except Comment.DoesNotExist:
                form.instance.parent = None

        try:
            form.instance.full_clean()
        except ValidationError as error:
            if hasattr(error, 'message_dict'):
                for field, _messages in error.message_dict.items():
                    for message in _messages:
                        form.add_error(field, message)
            else:
                form.add_error(None, error.messages)

            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.filter(parent__isnull=True)
        context = self.get_context_data(
            form=form, post=post,
            comments=comments
        )

        if 'reply_form' not in context:
            context['reply_form'] = CommentForm()

        messages.error(
            self.request,
            'Não foi possível salvar o comentário.'
        )

        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})


class CommentEdit(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/post_detail.html'
    success_message = 'Comentário atualizado com sucesso.'

    def form_valid(self, form):
        try:
            form.instance.full_clean()
        except ValidationError as error:
            if hasattr(error, 'message_dict'):
                for field, _messages in error.message_dict.items():
                    for message in _messages:
                        form.add_error(field, message)
            else:
                form.add_error(None, error.messages)

            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        comment = self.get_object()
        post = comment.post
        comments = post.comments.filter(parent__isnull=True)
        context = {
            'object': post,
            'post': post,
            'comments': comments,
            'form': CommentForm(),
            'reply_form': CommentForm(),
            'edit_form': form,
            'edit_comment_id': comment.id
        }

        messages.error(
            self.request,
            'Não foi possível atualizar o comentário.'
        )

        return self.render_to_response(context)

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser

    def get_success_url(self):
        messages.success(self.request, 'Comentário deletado com sucesso.')
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})
