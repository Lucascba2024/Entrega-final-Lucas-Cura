from django.db import models
from django.contrib.auth.models import User


#######sirve para mostrar en la pagina admnin los modelos con sus campos########este medoto###
def generate_str_method(self):
    """
    Generate __str__ method for a model instance
    """
    field_names = [field.name for field in self._meta.fields]
    values = ', '.join([f"{field_name}: {getattr(self, field_name)}" for field_name in field_names])
    return f"{self.__class__.__name__} - {values}"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField() 

    def __str__(self):
        return generate_str_method(self)

class profesores(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()  

    def __str__(self):
        return generate_str_method(self)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()  


    def __str__(self):
        return generate_str_method(self)

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)
    
    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"
