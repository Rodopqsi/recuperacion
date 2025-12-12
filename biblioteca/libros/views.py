from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Libro
from .serializers import LibroSerializer


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
