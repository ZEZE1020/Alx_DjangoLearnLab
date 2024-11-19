# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views      
from .views import SignUpView, register, login_view, login, logout_view



urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
