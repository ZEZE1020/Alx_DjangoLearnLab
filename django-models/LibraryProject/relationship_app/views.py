
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def list_books(request):
   books = Book.objects.all() 
   return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

def register (request): 
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

def is_admin(user):
    return user.userprofile.role == 'Admin'

def admin_view(request):
   return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def librarian_view(request):
   return render(request, 'librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

def member_view(request):
   return render(request, 'member_view.html')
   
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

