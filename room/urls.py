from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('room/', views.room, name='room'),
    path('user/', views.user, name='profile'),
]