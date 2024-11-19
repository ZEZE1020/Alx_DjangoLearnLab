
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def list_books(request):
   books = Book.objects.all() 
   return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

def register(request): 
   if request.method == "POST": 
      form = UserCreationForm(request.POST) 
   if form.is_valid(): 
      form.save() 
      username = form.cleaned_data.get('username') 
      password = form.cleaned_data.get('password1') 
      user = authenticate(username=username, password=password) 
      login(request, user) 
      return redirect('home') 
   else: 
      form = UserCreationForm() 
   return render(request, 'register.html', {'form': form})

def login_view(request): 
   if request.method == "POST":
       form = AuthenticationForm(data=request.POST) 
   if form.is_valid(): 
      user = form.get_user() 
      login(request, user) 
      return redirect('home') 
   else: 
      form = AuthenticationForm() 
   return render(request, 'login.html', {'form': form})

def logout_view(request): 
   logout(request) 
   return render(request, 'logout.html')
class SignUpView(generic.CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'relationship_app/register.html'