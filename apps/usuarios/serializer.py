from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'nombres','apellidos', 'genero', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'u_c', 'u_m']
        labels = {'username': 'Usuario', 'nombres': 'nombre usuario', 'apellidos': 'Apellido usuario',
                  'genero': 'Genero','email': 'Correo electrónico','is_active': 'Usuario Activo',
                  'is_staff': 'Acceso panel de administracion', 'is_superuser':'USUARIO ADMINISTRADOR', 'groups':'grupos a los que pertenece', 'user_permissions':'permisos que posee'
                 }       
        extra_kwargs = {
            'u_c':{'write_only':True},
            'u_m':{'write_only':True},
            }
        
    def create(self, validated_data, commit = True):
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
            u_c = validated_data['u_c'],
            u_m = validated_data['u_m'],
            
            )
        user.set_password(validated_data['password'])
        user.save()
        #user = super().save()
        user.save_m2m()
        Token.objects.create(user=user)
        return user
