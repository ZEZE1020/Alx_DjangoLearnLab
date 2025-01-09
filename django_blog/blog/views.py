from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post 
from .forms import PostForm
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

