from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Ganti 'home' dengan URL halaman utama setelah logout

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            message = {'error': 'Invalid credentials'}
            context = message
            return render(request, 'auth/login.html', context)
     
    return render(request, 'auth/login.html')

def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            message = {'error': 'Username already taken'}
            context = message
            return render(request, 'auth/register.html', context)
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        # Automatically log in the user after registration
        user = authenticate(username=username, password=password)
        login(request, user)
        
        return redirect('home')  # Replace 'home' with the URL name of your home page
        
    return render(request, 'auth/register.html')
