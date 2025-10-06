from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from posts.models import Post, Tag


class PostsByTagView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargsK['slug'])
        return Post.objects.filter(tags=tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return context
