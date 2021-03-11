from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.authtoken.models import Token


from .pagination import CustomPagination
from .serializer import *
from .models import User

# Create your views here.

class UserCreate(ListCreateAPIView):
    queryset = User.objects.all()
    # authentication_classes = (IsAuthenticated,)
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)
    serializer_class = UserSerializer
    pagination_class = CustomPagination

class ChangePasswordView(RetrieveUpdateAPIView):
    queryset= User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)

class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()    
    pagination_class = CustomPagination
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()        
        self.perform_destroy(instance)        
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupCreate(ListCreateAPIView):
    model = Group
    serializer_class = GrupoSerializer       
    pagination_class = CustomPagination
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)    
    queryset = Group.objects.all()
    #permisos extras
    # extra_perms_map = {
    #   'GET': ["can_view_groups"],
    #  }
    

class DetailGroup(RetrieveUpdateDestroyAPIView):
    serializer_class = GrupoSerializer
    queryset = Group.objects.all()    
    pagination_class = CustomPagination
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)