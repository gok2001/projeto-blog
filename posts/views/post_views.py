from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from posts.forms import PostForm, CommentForm
from posts.models import Post


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
