
from django.contrib import admin
from django.urls import path

from .views import *





urlpatterns = [
    path('mywallet/', mywallet,),
    path('', main, name='main'),
    path('main_detail', main_detail, name='main_detail'),
    path('main_upload', main_upload, name='main_upload'),
    path('contentsdetail/<int:id>', contentsdetail, name='contentsdetail'),
    path('contentstran/', contentstran, name='contentstran'),
    path('oauth', oauth, name='oauth'),
    path('login/', login, name='login'),
    path('transaction/', transaction),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('createaccount/', createaccount, name='createaccount'),
    path('contentsupload/', contentsupload, name='contentsupload'),
    path('mypage/', mypage, name='mypage'),
    path('contentsboard/', contentsboard,   name='contentsboard'),
    path('searchcontents/', searchcontents, name='searchcontents'),
]
