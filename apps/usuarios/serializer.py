from apps.usuarios import permissions

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Group

from .models import User

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User        
        fields = ['id','username', 'password', 'nombres','apellidos', 'genero', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']        
        extra_kwargs = {'password':{'write_only':True}}        
           
    def create(self, validated_data, commit= True):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            nombres = validated_data['nombres'],
            apellidos = validated_data['apellidos'],
            genero = validated_data['genero'],
            is_active = validated_data['is_active'],
            is_staff = validated_data['is_staff'],
            is_superuser = validated_data['is_superuser'],
            groups = validated_data['groups'],
            user_permissions = validated_data['user_permissions'],
            )
        user.set_password(validated_data['password'])

        returnedQueryset = validated_data('groups')
        
        for g in returnedQueryset.iterator():
            user.user_groups.add(g)
        user.save()                
        
        # self.save_m2m()
        Token.objects.create(user=user)

        return user
    
#gestion de grupos

class GrupoSerializer(serializers.ModelSerializer):
    # user = serializer.CharField
    # user = serializers.ForeignKey(User, )
    class Meta:
        model = Group
        fields = ['id','name','creator']
