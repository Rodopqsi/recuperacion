from .models import Libro, Autor
from rest_framework import serializers


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre']


class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), source='autor', write_only=True, required=False)

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'autor_id', 'imagen', 'fecha_publicacion']
    