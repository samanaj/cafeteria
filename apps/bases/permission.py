from rest_framework.permissions import DjangoModelPermissions

class BaseModelPerm(DjangoModelPermissions):
    # def __init__(self):
    #     self.perms_map = copy.deepcopy(self.perms_map) # you need deepcopy when you inherit a dictionary type 
    #     self.perms_map['GET'] = ['%(app_label)s.view_%(Group)s']
        
    def get_custom_perms(self, method, view):
        app_name = view.model._meta.app_label
        return [app_name+"."+perms for perms in view.extra_perms_map.get(method, [])]

    def has_permission(self, request, view):
        perms = self.get_required_permissions(request.method, view.model)
        perms.extend(self.get_custom_perms(request.method, view))
        return (request.user and (request.user.is_authenticated() or not self.authenticated_users_only) and request.user.has_perms(perms))

# class DjangoModelPermissionsStrict(DjangoModelPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(Group)s'],
#         'OPTIONS': [],
#         'HEAD': [],
#         'POST': ['%(app_label)s.add_%(Group)s'],
#         'PUT': ['%(app_label)s.change_%(Group)s'],
#         'PATCH': ['%(app_label)s.change_%(Group)s'],
#         'DELETE': ['%(app_label)s.delete_%(Group)s'],
#     }