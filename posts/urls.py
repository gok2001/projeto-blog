from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('/posts/<int:post_id>/', views.PostDetail.as_view(), name='post_detail'),
]
