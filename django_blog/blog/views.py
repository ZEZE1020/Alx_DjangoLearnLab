from django.shortcuts import render

# Create your views here.
# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

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
