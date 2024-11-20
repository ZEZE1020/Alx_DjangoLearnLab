# relationship_app/urls.py

from django.urls import path


from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views      
from .views import SignUpView
from .views import register
from .views import login_view
from .views import login
from .views import logout_view



urlpatterns = [
    path('register/', register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
]
