
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import UserCreate

urlpatterns = [
    path('user/add/', UserCreate.as_view(), name='user-add'),
    # path('user/add', UserCreate.as_view(), name='user-add'),
    # path('user/add', UserCreate.as_view(), name='user-add'),
]

