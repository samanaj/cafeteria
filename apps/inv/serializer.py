from rest_framework import serializers

from .models import Categoria, SubCategoria
 
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = ('descripcion', 'estado')

class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= SubCategoria
        fields = ('categoria', 'descripcion', 'estado')