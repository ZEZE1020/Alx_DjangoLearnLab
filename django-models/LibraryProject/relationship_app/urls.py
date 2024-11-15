# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views      
from .views import SignUpView


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', SignUpView.as_view(), name='register'),
]
