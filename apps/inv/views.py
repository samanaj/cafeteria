from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from rest_framework import status
from rest_framework.response import Response

from .models import Categoria, SubCategoria

from .serializer import CategoriaSerializer, SubCategoriaSerializer

from rest_framework import viewsets

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)

class subCategoriaViewSet(viewsets.ModelViewSet):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer

class HelloView(APIView):
    permission_classes = (DjangoModelPermissions, IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

