from decimal import Decimal

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase

from patrimonio.models import (BienFuente, BienPatrimonial, Categoria, FuenteDocumental,
                               TipoFuente, TipoPatrimonio)


class Semana1(TestCase):
    def setUp(self):
        call_command("seed")
        self.b = BienPatrimonial.objects.create(
            nombre="Plaza Murillo", descripcion="x", categoria=Categoria.objects.first(),
            tipo_patrimonio=TipoPatrimonio.objects.get(nombre="Material"),
            latitud=Decimal("-16.4958"), longitud=Decimal("-68.1334"))

    def test_pt02_sin_fuente(self):
        self.assertTrue(any("fuente" in e for e in self.b.errores_publicacion()))

    def test_pt03_fuera_de_zona(self):
        self.b.latitud = Decimal("-10.0")
        self.assertTrue(any("fuera" in e for e in self.b.errores_publicacion()))

    def test_pt04_publicacion_visible_en_api(self):
        f = FuenteDocumental.objects.create(titulo="t", tipo_fuente=TipoFuente.objects.first(),
                                            fecha_consulta="2026-10-11")
        BienFuente.objects.create(bien=self.b, fuente=f)
        self.assertEqual(self.b.errores_publicacion(), [])
        self.assertEqual(self.client.get("/api/bienes/").json()["count"], 0)  # borrador no es público
        self.b.estado_publicacion = "publicado"
        self.b.save()
        self.assertEqual(self.client.get("/api/bienes/").json()["count"], 1)

    def test_pt21_editor_sin_usuarios(self):
        u = User.objects.create_user("ed", password="x", is_staff=True)
        u.groups.add(Group.objects.get(name="Editor"))
        self.client.force_login(u)
        self.assertEqual(self.client.get("/admin/patrimonio/bienpatrimonial/").status_code, 200)
        self.assertEqual(self.client.get("/admin/auth/user/").status_code, 403)
