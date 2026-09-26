from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, LoginForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')

  else:
    form = SignUpForm()
    
  return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
  if request.method == "POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('dashboard')
  else:
    form = LoginForm()
  return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
  return render(request, 'accounts/dashboard.html')

@login_required
def update_profile(request):
  if request.method == "POST":
    form = ProfileUpdateForm(request.POST, instance=request.user)

    if form.is_valid():
      form.save()
      return redirect('dashboard')
  else:
    form = ProfileUpdateForm(instance=request.user)

  return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def delete_profile(request):
  if request.method == "POST":
    request.user.delete()
    return redirect('signup')

  return render(request, 'accounts/delete_profile.html')