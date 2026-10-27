from django.conf import settings
from django.db import models
from django.db.models import Q

ESTADOS_BIEN = ["borrador", "revision", "publicado", "desactivado"]


class Catalogo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Categoria(Catalogo):
    descripcion = models.TextField(blank=True)

    class Meta:
        db_table = "categoria"


class TipoPatrimonio(Catalogo):
    class Meta:
        db_table = "tipo_patrimonio"


class TipoFuente(Catalogo):
    class Meta:
        db_table = "tipo_fuente"


class TipoReporte(Catalogo):
    class Meta:
        db_table = "tipo_reporte"


class EstadoReporte(Catalogo):
    es_final = models.BooleanField(default=False)

    class Meta:
        db_table = "estado_reporte"


class Licencia(Catalogo):
    url = models.URLField(blank=True)

    class Meta:
        db_table = "licencia"


class ZonaPiloto(models.Model):
    nombre = models.CharField(max_length=120)
    lat_min = models.DecimalField(max_digits=9, decimal_places=6)
    lat_max = models.DecimalField(max_digits=9, decimal_places=6)
    lon_min = models.DecimalField(max_digits=9, decimal_places=6)
    lon_max = models.DecimalField(max_digits=9, decimal_places=6)
    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "zona_piloto"

    def contiene(self, lat, lon):
        return self.lat_min <= lat <= self.lat_max and self.lon_min <= lon <= self.lon_max

    def __str__(self):
        return self.nombre


class FuenteDocumental(models.Model):
    titulo = models.CharField(max_length=300)
    autor_institucion = models.CharField(max_length=200, blank=True)
    tipo_fuente = models.ForeignKey(TipoFuente, on_delete=models.PROTECT)
    url_referencia = models.CharField(max_length=500, blank=True)
    fecha_consulta = models.DateField()

    class Meta:
        db_table = "fuente_documental"

    def __str__(self):
        return self.titulo


class BienPatrimonial(models.Model):
    ESTADOS = [(e, e.capitalize()) for e in ESTADOS_BIEN]
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo_patrimonio = models.ForeignKey(TipoPatrimonio, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    zona_piloto = models.ForeignKey(ZonaPiloto, null=True, blank=True, on_delete=models.PROTECT)
    direccion_referencia = models.CharField(max_length=250, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    estado_publicacion = models.CharField(max_length=12, choices=ESTADOS, default="borrador")
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fuentes = models.ManyToManyField(FuenteDocumental, through="BienFuente", related_name="bienes")

    class Meta:
        db_table = "bien_patrimonial"
        constraints = [
            models.CheckConstraint(condition=Q(estado_publicacion__in=ESTADOS_BIEN), name="ck_estado_publicacion"),
            models.CheckConstraint(
                condition=Q(latitud__isnull=True) | Q(latitud__gte=-90, latitud__lte=90), name="ck_latitud"),
            models.CheckConstraint(
                condition=Q(longitud__isnull=True) | Q(longitud__gte=-180, longitud__lte=180), name="ck_longitud"),
        ]

    def __str__(self):
        return self.nombre

    def errores_publicacion(self):
        """RN-02 y RN-03: devuelve la lista de motivos por los que no se puede publicar."""
        e = []
        if not self.descripcion:
            e.append("Falta la descripción.")
        if not self.fuentes.exists():
            e.append("Requiere al menos una fuente con fecha de consulta.")
        if self.recursos.filter(Q(autor="") | Q(licencia__isnull=True)).exists():
            e.append("Hay imágenes sin autor o licencia.")
        if self.tipo_patrimonio.nombre.lower() == "material":
            if self.latitud is None or self.longitud is None:
                e.append("Un bien material requiere coordenadas.")
            else:
                z = self.zona_piloto or ZonaPiloto.objects.filter(activa=True).first()
                if not z or not z.contiene(self.latitud, self.longitud):
                    e.append("Las coordenadas están fuera del área piloto.")
        return e


class BienFuente(models.Model):
    bien = models.ForeignKey(BienPatrimonial, on_delete=models.CASCADE)
    fuente = models.ForeignKey(FuenteDocumental, on_delete=models.PROTECT)
    nota = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = "bien_fuente"
        constraints = [models.UniqueConstraint(fields=["bien", "fuente"], name="uq_bien_fuente")]


class RecursoMultimedia(models.Model):
    bien = models.ForeignKey(BienPatrimonial, on_delete=models.CASCADE, related_name="recursos")
    archivo = models.ImageField(upload_to="bienes/")
    texto_alternativo = models.CharField(max_length=250, blank=True)
    autor = models.CharField(max_length=150)
    licencia = models.ForeignKey(Licencia, on_delete=models.PROTECT)
    es_portada = models.BooleanField(default=False)

    class Meta:
        db_table = "recurso_multimedia"


class HistorialEstadoBien(models.Model):
    bien = models.ForeignKey(BienPatrimonial, on_delete=models.CASCADE, related_name="historial")
    estado_anterior = models.CharField(max_length=12, blank=True)
    estado_nuevo = models.CharField(max_length=12)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "historial_estado_bien"


# --- Modelos de las semanas 3 (M3 y M4); se crean ahora para tener el esquema completo ---
class Actividad(models.Model):
    bien = models.ForeignKey(BienPatrimonial, on_delete=models.CASCADE, related_name="actividades")
    enunciado = models.TextField()
    retroalimentacion = models.TextField()
    puntos = models.PositiveSmallIntegerField(default=10)
    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "actividad"


class OpcionActividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="opciones")
    texto = models.CharField(max_length=250)
    es_correcta = models.BooleanField(default=False)

    class Meta:
        db_table = "opcion_actividad"
        constraints = [models.UniqueConstraint(
            fields=["actividad"], condition=Q(es_correcta=True), name="uq_una_correcta")]


class ReporteCiudadano(models.Model):
    bien = models.ForeignKey(BienPatrimonial, on_delete=models.PROTECT)
    tipo_reporte = models.ForeignKey(TipoReporte, on_delete=models.PROTECT)
    estado = models.ForeignKey(EstadoReporte, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reporte_ciudadano"


class HistorialEstadoReporte(models.Model):
    reporte = models.ForeignKey(ReporteCiudadano, on_delete=models.CASCADE, related_name="historial")
    estado_anterior = models.ForeignKey(EstadoReporte, on_delete=models.PROTECT, related_name="+")
    estado_nuevo = models.ForeignKey(EstadoReporte, on_delete=models.PROTECT, related_name="+")
    revisado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    nota = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "historial_estado_reporte"
