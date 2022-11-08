from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'room/home.html')

def explore(request):
    return render(request, 'room/explore.html')

def login(request):
    return render(request, 'room/login.html')

def room(request):
    return render(request, 'room/room.html')

def user(request):
    return render(request, 'room/user.html')