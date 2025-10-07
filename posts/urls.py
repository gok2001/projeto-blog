from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('search/', views.PostSearchView.as_view(), name='search'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),

    # Comentários
    path('post/<int:post_id>/comment/',
         views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/edit/', views.CommentEdit.as_view(), name='comment_edit'),
    path('post/<int:pk>/delete/',
         views.CommentDelete.as_view(), name='comment_delete'),

    # Tags e Categorias
    path('category/<slug:slug>/',
         views.PostsByCategoryView.as_view(), name='category'),
    path('tag/<slug:slug>/', views.PostsByTagView.as_view(), name='tag')
]
