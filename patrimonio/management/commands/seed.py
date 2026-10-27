from datetime import date
from decimal import Decimal

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from patrimonio.models import (Categoria, EstadoReporte, Licencia, TipoFuente,
                               TipoPatrimonio, TipoReporte, ZonaPiloto)

CATALOGOS = {
    Categoria: ["Arquitectura religiosa", "Arquitectura civil", "Espacio público", "Fiesta y tradición"],
    TipoPatrimonio: ["Material", "Inmaterial"],
    TipoFuente: ["Norma", "Publicación", "Inventario", "Sitio web", "Entrevista", "Otro"],
    TipoReporte: ["Deterioro", "Información incorrecta", "Acceso restringido", "Otro"],
    Licencia: ["Propia", "CC BY 4.0", "CC BY-SA 4.0", "Dominio público"],
}


class Command(BaseCommand):
    help = "Carga catálogos, zona piloto y grupos Editor/Administrador (idempotente)."

    def handle(self, *a, **o):
        for modelo, nombres in CATALOGOS.items():
            for n in nombres:
                modelo.objects.get_or_create(nombre=n)
        for n, final in [("Nuevo", False), ("En revisión", False), ("Atendido", True), ("Descartado", True)]:
            EstadoReporte.objects.get_or_create(nombre=n, defaults={"es_final": final})
        # Caja geográfica APROXIMADA (verificar con IDE La Paz y documentar)
        ZonaPiloto.objects.get_or_create(nombre="Eje central (aprox.)", defaults=dict(
            lat_min=Decimal("-16.5120"), lat_max=Decimal("-16.4900"),
            lon_min=Decimal("-68.1450"), lon_max=Decimal("-68.1200")))
        dominio = Permission.objects.filter(content_type__app_label="patrimonio")
        Group.objects.get_or_create(name="Editor")[0].permissions.set(dominio)
        extra = Permission.objects.filter(content_type__app_label__in=["auth", "admin"])
        ids = list(dominio.values_list("pk", flat=True)) + list(extra.values_list("pk", flat=True))
        Group.objects.get_or_create(name="Administrador")[0].permissions.set(ids)
        self.stdout.write(self.style.SUCCESS("Seed completo."))
