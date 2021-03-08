# def populate_models(sender, **kwargs):
#     from django.apps import apps
#     from .apps import UsuariosConfig
#     from django.contrib.auth.models import Group, Permission
#     from django.contrib.contenttypes.models import ContentType

#     group_app, created = Group.objects.get_or_create(name=UsuariosConfig.name)

#     models = apps.all_models[UsuariosConfig.name]
#     for model in models:
#         content_type = ContentType.objects.get(
#             app_label=UsuariosConfig.name,
#             model=model
#         )
#         permissions = Permission.objects.filter(content_type=content_type)
#         group_app.permissions.add(*permissions)