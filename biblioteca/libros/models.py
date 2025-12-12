from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True, blank=True, related_name='libros')
    imagen = models.ImageField(upload_to='imagenes/')
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return self.titulo


class Autor(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre