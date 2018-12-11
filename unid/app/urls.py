from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('index/', index),
    path('contentsmain1/', contentsmain1),
]
