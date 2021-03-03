from django.db import models
from apps.bases.models import BaseModel

from cafeteria.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class Categoria(BaseModel):   
    descripcion = models.CharField(max_length=100, help_text='Descripción de la Categoría', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(Categoria, self).save()


    class Meta:
        verbose_name_plural= "Categorias"

class SubCategoria(BaseModel):   
    descripcion = models.CharField(max_length=100, help_text='Descripción de la Sub-Categoría', unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(SubCategoria, self).save()


    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion')

class Marca(BaseModel):   
    descripcion = models.CharField(max_length=100, help_text='Descripción de la Marca', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(Marca, self).save()


    class Meta:
        verbose_name_plural= "Marcas"


class UnidadMedida(BaseModel):   
    descripcion = models.CharField(max_length=100, help_text='Descripción de la Unidad de Medida', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(UnidadMedida, self).save()


    class Meta:
        verbose_name_plural= "Unidad de medidas"


class Sabor(BaseModel):   
    sabor = models.CharField(max_length=30, help_text='Descripción del Sabor', unique=True)
    descripcion = models.CharField(max_length=100, help_text='observaciones', unique=True)

    def __str__(self):
        return '{}:{}'.format(self.sabor, self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.sabor = self.sabor.upper()
        self.descripcion = self.descripcion.upper()  
        super(Sabor, self).save()


    class Meta:
        verbose_name_plural= "Sabores"

class Decoracion(BaseModel):   
    decoracion = models.CharField(max_length=30, help_text='Descripción de la decoración', unique=True)
    estilo = models.CharField(max_length=100, help_text='descripcion del estilo')
    image = models.ImageField(upload_to='decoracion/%Y/%m/%d', blank=True, null=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return '{}:{}'.format(self.sabor, self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        self.estilo = self.estilo.upper()  
        super(Decoracion, self).save()


    class Meta:
        verbose_name_plural= "Decoraciones"


class Caducidad(BaseModel):   
    vida_prod = models.CharField(max_length=30, help_text='Tiempo de vida del producto', unique=True)   
    
    def __str__(self):
        return '{}'.format(self.vida_prod)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.vida_prod = self.vida_prod.upper()  
        super(Caducidad, self).save()


    class Meta:
        verbose_name_plural= "Caducidades"

class Oferta(BaseModel):   
    descripcion = models.CharField(max_length=30, help_text='Nombre de la Oferta', unique=True)   
    precioOferta= models.FloatField(default=0)
    f_inicio = models.DateField()
    f_fin = models.DateField()

    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(Oferta, self).save()


    class Meta:
        verbose_name_plural= "ofertas"


class Producto(BaseModel):
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    decoracion = models.ForeignKey(Decoracion, on_delete=models.CASCADE)
    caducidad = models.ForeignKey(Caducidad, on_delete=models.CASCADE)
    oferta = models.ManyToManyField(Oferta)
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        us = get_current_user()
        if us is not None:
            if not self.pk:
                self.u_c = us
            else:
                self.u_m = us
        self.descripcion = self.descripcion.upper()  
        super(Producto, self).save()


    class Meta:
        verbose_name_plural= "Productos"