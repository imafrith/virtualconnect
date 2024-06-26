from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('room/', views.room, name='room'),
    path('lobby/',views.lobby, name='lobby'), 
    path('get_token/', views.getToken),
    
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    
]
