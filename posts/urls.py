from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),

    # Comentários
    path('post/<int:post_id>/comment/', views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/edit/', views.CommentEdit.as_view(), name='comment_edit'),
    path('post/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
