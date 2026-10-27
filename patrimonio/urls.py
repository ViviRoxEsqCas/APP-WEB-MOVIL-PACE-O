from django.urls import path

from . import views

urlpatterns = [
    path("bienes/", views.BienList.as_view()),
    path("bienes/<int:pk>/", views.BienDetalle.as_view()),
    path("categorias/", views.CategoriaList.as_view()),
]
