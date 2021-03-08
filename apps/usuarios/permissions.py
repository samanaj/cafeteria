from rest_framework import permissions
from .apps import UsuariosConfig
from django.contrib.auth.models import Group

from rest_framework.exceptions import PermissionDenied

#group = Group.objects.all()

class IsOwner(permissions.BasePermission):
       message = "Usuario no es el propietario"
       #print (group)
       def has_object_permission(self, request, view, obj):
              print(obj.owner)
              print(request.user)
              if request.method in permissions.SAFE_METHODS:
                     return True
              return request.user == obj.owner

def is_in_group_app1(user):
    return user.groups.filter(name=UsuariosConfig.name).exists() 

""" esta es otra forma de trabajar con permisos"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the movie
        return obj.u_c == request.user


class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        message = 'You must be authenticated'
        is_it = bool(request.user and request.user.is_authenticated)
        if is_it:
            return is_it
        else:
            raise PermissionDenied(detail=message)