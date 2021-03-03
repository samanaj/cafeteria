from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response

from .models import Categoria
from .serializer import CategoriaSerializer
from rest_framework import viewsets

 
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# class CategoriaAdd(APIView):
#     def post(self,request,cat_pk):
#         descripcion = request.data.get("descripcion")
#         estado = request.data.get("estado")
#         data = {'descripcion':descripcion, 'estado':estado}
#         serializer = CategoriaSerializer(data=data)
#         if serializer.is_valid():
#             subcat = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)