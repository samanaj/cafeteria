from apps.usuarios import permissions

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Group

from .models import User

class GroupSerialiezer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = '__all__'

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
        user.user_permissions.clear()
        for p in permis_data:
            user.user_permissions.add(p)
        #grupos
        user.groups.clear()
        # user.save_m2m()
        for g in groups_data:
            user.groups.add(g)
       
        Token.objects.create(user=user)
        return user

    #actualizar
    def update(self,instance,validated_data):
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)
        
        instance.save()

#USER UPDATEA
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['username', 'nombres','apellidos', 'genero', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']        

    # password = ReadOnlyPasswordHashField()

    # nombres = serializers.CharField()
    # apellidos = serializers.CharField()
    # genero = serializers.CharField()
    # is_staff = serializers.BooleanField()
    # is_active = serializers.BooleanField()
    # is_superuser =serializers.BooleanField()
    # groups = GroupSerialiezer(many=True)

    # user_permissions = serializers.ManyToManyField(to='auth.Permission')
    

    def update(self, instance, validated_data):
        # groups_data = validated_data.pop('groups')
        # permis_data = validated_data.pop('user_permissions')
        groups_data = validated_data.get('groups', instance.groups)
        permis_data = validated_data.get('user_permissions', instance.user_permissions)
       
        inst = User (
            nombres = validated_data.get('nombres', instance.nombres),
            apellidos = validated_data.get('apellidos', instance.apellidos),
            genero = validated_data.get('genero', instance.genero),
            email = validated_data.get('email', instance.email),
            is_staff = validated_data.get('is_staff', instance.is_staff),
            is_active = validated_data.get('is_active', instance.is_active),
            is_superuser = validated_data.get('is_superuser', instance.is_superuser),        
        )

        inst.save()
        # #user.user_permissions.clear()
        for p in permis_data:
            inst.user_permissions.add(p)
        # #grupos
        # #user.groups.clear()
        # # user.save_m2m()
        for g in groups_data:
            inst.groups.add(g)       
        return inst


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





class GrupoSerializer(serializers.ModelSerializer):#    
    class Meta:
        model = Group
        fields = ['id','name']
