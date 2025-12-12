from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.ProductoListCreate.as_view(), name='libro-list-create'),
    path('libros/<int:pk>/', views.LibroDetail.as_view(), name='libro-detail'),
]
