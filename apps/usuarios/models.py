from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from apps.bases.models import BaseModel2
from crum import get_current_user

class User(BaseModel2, AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
     )
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser =models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    #esto hace que pida el campo a requerir en la creación.
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    
    #funcion para que me retorne el username, nombre corto
    def get_short_name(self):
        return self.username
    #funcion para que me retorne el nombre y el apellido completo.
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, commit = True):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        super(User, self).save()        
        return User