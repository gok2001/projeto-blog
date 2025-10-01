from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm, CommentForm
from .models import Post, Comment


class Index(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(parent__isnull=True)
        context['reply_form'] = CommentForm()
        context['form'] = CommentForm()

        return context


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

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

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})


class CommentEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_edit.html'

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
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.post.pk})
