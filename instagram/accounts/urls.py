
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html'}),

]
