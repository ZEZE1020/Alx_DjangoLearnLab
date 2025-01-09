# blog/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm): 
  class Meta: 
    model = Post 
    fields = ['title', 'content']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['title','content', 'tags']