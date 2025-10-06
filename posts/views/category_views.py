from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from posts.models import Post, Category


class PostsByCategoryView(ListView):
    model = Post
    template = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context
