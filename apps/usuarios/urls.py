
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import UserCreate, UserDetailApiView, ChangePasswordView, GroupCreate, DetailGroup

urlpatterns = [
    #users
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('user/edit/<pk>', UserDetailApiView.as_view(), name='user-edit'),
    path('user/uppass/<pk>', ChangePasswordView.as_view(), name='user-chpass'),
    
    #Groups
    path('group/add/', GroupCreate.as_view(), name='group-add'),
    path('group/edit/<pk>', DetailGroup.as_view(), name='group-edit'),
]

