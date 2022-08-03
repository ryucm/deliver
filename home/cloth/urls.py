from django.urls import path
from . import views

urlpattern = [
    path('', views.member_list, name = 'member_list'),
]