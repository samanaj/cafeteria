from django.apps import AppConfig
# from django.db.models.signals import post_migrate


class UsuariosConfig(AppConfig):
    name = 'usuarios'

    # def ready(self):
    #         from .signals import populate_models
    #         post_migrate.connect(populate_models, sender=self)