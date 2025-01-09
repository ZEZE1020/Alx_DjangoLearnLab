from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
# blog/views.py

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      if user_form.is_valid():
        user_form.save()
        return redirect('profile')
      else:
           user_form = UserUpdateForm(request.POST, instance=request.user)
           context = {
            'user_form': user_form,
           }
    return render(request, 'blog/profile.html')


class PostListView(ListView):
  model = Post
  template_name = 'blog/base.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5

class PostDetailView(DetailVIew):
  model = Post
  template_name = 'blog/post_detail.html' # Default: <app_name>/<model_name>_detail.html 
  class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post 
    form_class = PostForm
    template_name = 'blog/post_form.html' 
    def form_valid(self, form):
       form.instance.author = self.request.user 
       return super().form_valid(form) 
       
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
  model = Post 
  form_class = PostForm 
  template_name = 'blog/post_form.html' 

  def form_valid(self, form):
     form.instance.author = self.request.user
  return super().form_valid(form)
  
  def test_func(self): 
    post = self.get_object()
  return self.request.user == post.author 
     
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
  model = Post 
  template_name = 'blog/post_confirm_delete.html' 
  success_url = reverse_lazy('post-list')
   
  def test_func(self):
     post = self.get_object() 
  return self.request.user


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post-detail', pk=comment.post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post-detail', pk=comment.post.pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('post-detail', pk=comment.post.pk)
    return render(request, 'blog/delete_comment.html', {'comment': comment})
