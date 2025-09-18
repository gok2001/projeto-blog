from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:post_id>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
]
