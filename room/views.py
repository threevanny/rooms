from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupUserForm
from .models import Room, User, Profile


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('explore')
    return render(request, 'room/home.html')

def explore(request):
    return render(request, 'room/explore.html')

def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'room/room.html', {'room': room })

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, id_user=user.id)
    # get rooms of user where status is public
    #rooms = Room.objects.filter(id_user=user.id, status='public')
    return render(request, 'room/profile.html', { 'user_': user , 'profile': profile, })

def signin(request):
    if request.user.is_authenticated:
        return redirect('explore')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('explore')
        else:
            return redirect('login')
    else:
        return render(request, 'room/login.html')

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('explore')
    
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

            # if profile not exist then create new profile

            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('room')
    else:
        form = SignupUserForm()
    return render(request, 'room/signup.html', {'form': form})