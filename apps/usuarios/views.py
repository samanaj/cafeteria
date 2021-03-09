from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .permissions import IsOwner
# from rest_framework.permissions import IsAuthenticated


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

class ChangePasswordView(RetrieveUpdateAPIView):
    queryset= User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]

class UserUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()    
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    # def update(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    # queryset
    user = User.objects.filter(id = pk).first()
    # validation
    if user:
        if request.method == 'GET': 
            user_serializer = UserUpdateSerializer(user)
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            user_serializer = UserUpdateSerializer(user,data = request.data) # <<--------------- SE ENVÍA LA INSTANCIA
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)



    # def update(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_200_OK)



# @api_view(['GET','PUT','DELETE'])
# def user_detail_api_view(request,pk=None):
#     # queryset
#     user = User.objects.filter(id = pk).first()

#     # validation
#     if user:

#         # retrieve
#         if request.method == 'GET': 
#             user_serializer = UserSerializer(user)
#             return Response(user_serializer.data,status = status.HTTP_200_OK)
        
#         # update
#         elif request.method == 'PUT':
#             user_serializer = UserSerializer(user,data = request.data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data,status = status.HTTP_200_OK)
#             return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
#         # delete
#         elif request.method == 'DELETE':
#             user.delete()
#             return Response({'message':'Usuario Eliminado correctamente!'},status = status.HTTP_200_OK)
    
#     return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)