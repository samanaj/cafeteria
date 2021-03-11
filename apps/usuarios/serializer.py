from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Group

from .models import User

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User        
        fields = ['id','username', 'password', 'nombres','apellidos', 'genero', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']        
        extra_kwargs = {'password':{'write_only':True}}

           
    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        permis_data = validated_data.pop('user_permissions')
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
            nombres = validated_data['nombres'],
            apellidos = validated_data['apellidos'],
            genero = validated_data['genero'],
            is_active = validated_data['is_active'],
            is_staff = validated_data['is_staff'],
            is_superuser = validated_data['is_superuser'],
                       
            )
        user.set_password(validated_data['password'])
                      
        user.save()
        #permissos
        # user.user_permissions.clear()
        for p in permis_data:
            user.user_permissions.add(p)
        #grupos
        # user.groups.clear()
        # user.save_m2m()
        for g in groups_data:
            user.groups.add(g)
        #creacion de token
        Token.objects.create(user=user)
        return user

#USER UPDATEA

class UserUpdateSerializer(serializers.ModelSerializer):
    # shop = serializers.CharField()
    class Meta:
        model = User
        fields = ['id','username', 'password', 'nombres','apellidos', 'genero', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']
        
    def update(self, instance, validated_data):
         return super().update(instance, validated_data)


#gestion de contraseña   
class ChangePasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    old_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'old_password', 'new_password','confirm_password']

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)

        if not validated_data['new_password']:
              raise serializers.ValidationError({'new_password': 'not found'})

        if not validated_data['old_password']:
              raise serializers.ValidationError({'old_password': 'not found'})

        if not instance.check_password(validated_data['old_password']):
              raise serializers.ValidationError({'old_password': 'wrong password'})

        if validated_data['new_password'] != validated_data['confirm_password']:
            raise serializers.ValidationError({'passwords': 'passwords do not match'})

        if validated_data['new_password'] == validated_data['confirm_password'] and instance.check_password(validated_data['old_password']):
            # instance.password = validated_data['new_password'] 
            # print(instance.password)
            instance.set_password(validated_data['new_password'])
            # print(instance.password)
            instance.save()
            return instance
        return instance


# #gestion de grupos
class GrupoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = ['id','name']
