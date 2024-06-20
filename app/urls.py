from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from .views import userController,homeController,blabController,resetController,toolsController

urlpatterns = [
    path('', homeController.home),
    path('login', userController.login, name='login'),
    path('password-hint', userController.showPasswordHint, name='passwordHint'),
    path('logout', userController.logout, name='logout'),
    path('register', userController.register, name='register'),
    path('register-finish', userController.registerFinish, name='registerFinish'),
    path('feed', blabController.feed, name='feed'),
    path('morefeed', blabController.morefeed, name='morefeed'),
    path('blabbers', blabController.blabbers, name='blabbers'),
    path('profile', userController.profile, name='profile'),
    path('tools', toolsController.tools, name='tools'),
    #path('notImplemented', view.notImplemented, name='notImplemented'),
    path('reset', resetController.reset, name='reset'),
    path('downloadprofileimage', userController.downloadImage, name='downloadProfileImage'),
    path('blab', blabController.blab, name='blab'),
]