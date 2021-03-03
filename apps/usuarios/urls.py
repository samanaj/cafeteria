
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views

from rest_framework_simplejwt import views as jwt_views

from .views import *

urlpatterns = [
    path('user/add', UserCreate.as_view(), name='user-add'),
]