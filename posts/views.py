from django.shortcuts import render
from django.views import View

from .models import Post


class Index(View):
    post_class = Post
    template_name = 'posts/post_list.html'

    def get(self, request):
        posts = self.post_class.objects.all()

        return render(request, self.template_name, {'posts': posts})
    

class PostDetail(View):
    post_class = Post
    template_name = 'posts/post_detail.html'

    def get(self, request, post_id):
        post = self.post_class.objects.get(pk=post_id)

        return render(request, self.template_name, {'post': post})
