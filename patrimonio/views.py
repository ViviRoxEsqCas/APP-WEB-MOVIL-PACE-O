from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import BienPatrimonial, Categoria
from .serializers import BienDetalleSerializer, BienListSerializer, CategoriaSerializer


def publicados():  # RN-01: solo los publicados son públicos
    return BienPatrimonial.objects.filter(estado_publicacion="publicado")


class BienList(ListAPIView):
    serializer_class = BienListSerializer

    def get_queryset(self):
        qs = publicados().select_related("categoria", "tipo_patrimonio").order_by("nombre")
        p = self.request.query_params
        if p.get("categoria"):
            qs = qs.filter(categoria_id=p["categoria"])
        if p.get("q"):  # búsqueda simple; se refina en la semana 2 (tildes)
            qs = qs.filter(nombre__icontains=p["q"])
        return qs


class BienDetalle(RetrieveAPIView):
    serializer_class = BienDetalleSerializer

    def get_queryset(self):
        return publicados().prefetch_related("fuentes__tipo_fuente", "recursos__licencia")


class CategoriaList(ListAPIView):
    queryset = Categoria.objects.order_by("nombre")
    serializer_class = CategoriaSerializer
    pagination_class = None
