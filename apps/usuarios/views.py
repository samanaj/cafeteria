from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response

from .permissions import IsOwner
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .pagination import CustomPagination
from .serializer import *
from .models import User
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
# Create your views here.

class UserCreate(ListCreateAPIView):
    queryset = User.objects.all()
    # authentication_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    pagination_class = CustomPagination
