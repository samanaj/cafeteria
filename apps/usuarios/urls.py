
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import UserCreate, UserUpdateApiView, ChangePasswordView

urlpatterns = [
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('user/update/<pk>', UserUpdateApiView.as_view(), name='user-update'),
    path('user/uppass/<pk>', ChangePasswordView.as_view(), name='user-chpass'),
    
    #path('user/det/<pk>/',user_detail_api_view, name = 'usuario_detail_api_view')
    # path('user/add', UserCreate.as_view(), name='user-add'),
    # path('user/add', UserCreate.as_view(), name='user-add'),
]

