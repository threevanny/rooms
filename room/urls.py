from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('login/', views.login, name='login'),
    path('room/', views.room, name='room'),
    path('user/', views.user, name='user'),
]