from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import PostForm
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
    

class PostCreate(View):
    post_class = Post
    template_name = 'posts/post_create.html'

    def get(self, request):
        form = PostForm()

        context = {
            'form': form,
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = PostForm(request.POST)

        context = {
            'form': form,
    
        }

        if form.is_valid():
            form.save()
            return redirect('posts:index')
        
        return render(request, self.template_name, context)