from django.db import models
from django.conf import settings

from rest_framework.permissions import DjangoModelPermissions

# Create your models here.
class BaseModel(models.Model):
    estado = models.BooleanField(default=True)
    u_c = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
    f_c = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    u_m = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated')
    f_m = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class BaseModel2(models.Model):    
    u_c = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
    f_c = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    u_m = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated')
    f_m = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class OwnerModel(models.Model):    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BaseModelPerm(DjangoModelPermissions):
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map) # you need deepcopy when you inherit a dictionary type 
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        
    def get_custom_perms(self, method, view):
        app_name = view.model._meta.app_label
        return [app_name+"."+perms for perms in view.extra_perms_map.get(method, [])]

    def has_permission(self, request, view):
        perms = self.get_required_permissions(request.method, view.model)
        perms.extend(self.get_custom_perms(request.method, view))
        return (request.user and (request.user.is_authenticated() or not self.authenticated_users_only) and request.user.has_perms(perms))