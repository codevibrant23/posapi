from django.contrib import admin
from django.urls import path, include
from userauth import views


urlpatterns = [
    path('login/', views.user_login, name="Login Method"),
]