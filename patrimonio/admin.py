from django.apps import apps
from django.contrib import admin, messages

from .models import BienFuente, BienPatrimonial, HistorialEstadoBien, RecursoMultimedia


class BienFuenteInline(admin.TabularInline):
    model = BienFuente
    extra = 1


class RecursoInline(admin.TabularInline):
    model = RecursoMultimedia
    extra = 0


@admin.register(BienPatrimonial)
class BienAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "tipo_patrimonio", "estado_publicacion")
    list_filter = ("estado_publicacion", "categoria", "tipo_patrimonio")
    search_fields = ("nombre",)
    readonly_fields = ("creado_por",)
    inlines = [BienFuenteInline, RecursoInline]

    def save_model(self, request, obj, form, change):
        if change:
            obj._anterior = BienPatrimonial.objects.get(pk=obj.pk).estado_publicacion
        else:
            obj._anterior = ""
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)  # guarda fuentes e imágenes
        b = form.instance
        if b.estado_publicacion == "publicado":
            errores = b.errores_publicacion()
            if errores:  # RN-02 / RN-03: la publicación se bloquea
                b.estado_publicacion = "borrador"
                b.save(update_fields=["estado_publicacion"])
                messages.error(request, "No se puede publicar: " + " ".join(errores))
        if b.estado_publicacion != b._anterior:
            HistorialEstadoBien.objects.create(
                bien=b, estado_anterior=b._anterior,
                estado_nuevo=b.estado_publicacion, usuario=request.user)


for m in apps.get_app_config("patrimonio").get_models():
    if not admin.site.is_registered(m):
        admin.site.register(m)
