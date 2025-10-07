from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='posts:index'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path(
        'profile/edit_profile',
        views.EditProfileView.as_view(),
        name='edit_profile'
    ),
]
