from django.shortcuts import render
from django.views import View

from .models import Post


class Index(View):
    post_class = Post
    template_name = 'posts/post_list.html'

    def get(self, request):
        posts = self.post_class.objects.all()

        return render(request, self.template_name, {'posts': posts})
