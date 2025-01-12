from django.urls import path
from .views import RegisterView, CustomAuthToken, UserListView, follow_user, unfollow_user, ProfileView
from accounts.views import home 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'), 
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
