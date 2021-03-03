from django.db import models

# Create your models here.
from django.db import models


from django.conf import settings

# Create your models here.
class BaseModel(models.Model):
    estado = models.BooleanField(default=True)
    u_c = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
    f_c = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    u_m = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated')
    f_m = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True