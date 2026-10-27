from rest_framework import serializers

from .models import BienPatrimonial, Categoria, FuenteDocumental, RecursoMultimedia


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "nombre", "descripcion")


class FuenteSerializer(serializers.ModelSerializer):
    tipo_fuente = serializers.StringRelatedField()

    class Meta:
        model = FuenteDocumental
        fields = ("titulo", "autor_institucion", "tipo_fuente", "url_referencia", "fecha_consulta")


class RecursoSerializer(serializers.ModelSerializer):
    licencia = serializers.StringRelatedField()

    class Meta:
        model = RecursoMultimedia
        fields = ("archivo", "texto_alternativo", "autor", "licencia", "es_portada")


class BienListSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    tipo = serializers.StringRelatedField(source="tipo_patrimonio")

    class Meta:
        model = BienPatrimonial
        fields = ("id", "nombre", "categoria", "tipo", "latitud", "longitud")


class BienDetalleSerializer(BienListSerializer):
    fuentes = FuenteSerializer(many=True)
    imagenes = RecursoSerializer(many=True, source="recursos")

    class Meta(BienListSerializer.Meta):
        fields = BienListSerializer.Meta.fields + ("descripcion", "direccion_referencia", "fuentes", "imagenes")
