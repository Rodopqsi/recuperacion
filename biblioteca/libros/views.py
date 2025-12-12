from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer


class ProductoListCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = LibroSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibroDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return None

    def get(self, request, pk):
        libro = self.get_object(pk)
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibroSerializer(libro, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        libro = self.get_object(pk)
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibroSerializer(libro, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        libro = self.get_object(pk)
        if not libro:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AutorListCreate(APIView):
    def get(self, request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutorDetail(APIView):
    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return None

    def get(self, request, pk):
        autor = self.get_object(pk)
        if not autor:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    def put(self, request, pk):
        autor = self.get_object(pk)
        if not autor:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AutorSerializer(autor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autor = self.get_object(pk)
        if not autor:
            return Response(status=status.HTTP_404_NOT_FOUND)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
