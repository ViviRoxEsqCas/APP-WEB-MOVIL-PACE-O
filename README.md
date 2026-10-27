<p align="center">
  <img src="docs/capturas/banner.svg" alt="PACEÑO" width="100%">
</p>

<p align="center">
  <strong>Descubre, aprende y cuida el patrimonio cultural de La Paz.</strong><br>
  <sub>Taller de Proyecto · Informática · UMSA</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Estado-Semana%201%20de%204-8E5350?style=flat-square">
</p>

---

## Descripción

Aplicación web progresiva (PWA) con catálogo de fichas patrimoniales documentadas, mapa, actividades de opción múltiple y reportes ciudadanos revisados por un equipo editorial. Alcance: área piloto del eje central de La Paz (plaza Murillo, San Francisco y avenida Aniceto Arce), con 10 a 15 fichas.

## Tecnologías

Django · Django REST Framework · Django Admin · PostgreSQL · React + Vite y Leaflet (semana 2)

## Avance: Semana 1

- [x] Modelos de datos (16 tablas)
- [ ] Migraciones aplicadas en un entorno limpio
- [ ] Django Admin con grupos Editor y Administrador
- [ ] Validación de publicación de fichas
- [ ] API de lectura: `/api/bienes/` y `/api/categorias/`
- [ ] 5 a 8 fichas cargadas
- [ ] Pruebas PT-01 a PT-05 y PT-21

## Capturas

**Panel administrativo**

<img src="docs/capturas/01-panel-admin.png" width="80%">

**API de bienes**

<img src="docs/capturas/04-api-bienes.png" width="80%">

**API de categorías**

<img src="docs/capturas/05-api-categorias.png" width="80%">

## Instalación

Requisitos: Python, Git y PostgreSQL.

```powershell
git clone https://github.com/TU-USUARIO/paceno.git
cd paceno

py -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Configura las credenciales de PostgreSQL antes de migrar.

## Pruebas

```powershell
python manage.py test patrimonio
```

Resultados en `docs/pruebas/`.

---

<p align="center">
  <sub>Vivian Roxana Esquivel Castillo · Docente: Brígida Carvajal Blanco · La Paz, Bolivia</sub>
</p>
