from django.contrib import admin
from .models import Libro, Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'autor', 'fecha_publicacion')
