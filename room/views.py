from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupUserForm


# Create your views here.

def home(request):
    return render(request, 'room/home.html')

def explore(request):
    return render(request, 'room/explore.html')

def room(request):
    return render(request, 'room/room.html')

def user(request):
    return render(request, 'room/user.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('room')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('room')
        else:
            return redirect('login')
    else:
        return render(request, 'room/login.html')

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('room')
    else:
        form = SignupUserForm()
    return render(request, 'room/signup.html', {'form': form})