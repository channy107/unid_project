
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    url(r'^detail/(?P<post_id>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^update/(?P<post_id>[0-9]+)/$', post_update, name='post_update'),
    url(r'^delete/(?P<post_id>[0-9]+)/$', post_delete, name='post_delete'),
    url(r'^search/$', post_search, name='post_search'),                       #Ajax
    url(r'^likes/(?P<post_id>[0-9]+)/$', post_likes, name='post_likes'),      #Ajax
    url(r'^list/ajax/$', post_list_ajax, name='post_list_ajax'),

]
