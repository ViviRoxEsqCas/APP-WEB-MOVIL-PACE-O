# PACEÑO

<p align="center">
  <img src="docs/capturas/banner.svg" alt="PACEÑO — Geospatial Cultural Heritage Platform" width="100%">
</p>

<p align="center">
  <strong>Explora. Descubre. Preserva.</strong><br>
  Plataforma web móvil para la difusión y valoración del patrimonio cultural de La Paz, Bolivia.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=flat-square&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=flat-square&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Week%201%2F4-8B7CFF?style=flat-square">
</p>

---

## `01` / Overview

PACEÑO es un proyecto académico individual que busca conectar a la ciudadanía con el patrimonio cultural paceño mediante un catálogo digital, exploración geográfica, experiencias educativas y participación ciudadana.

**Alcance:** municipio de La Paz, Bolivia.

## `02` / Tech stack

| Componente | Tecnología |
|---|---|
| Backend | Python · Django |
| Base de datos | PostgreSQL |
| Control de versiones | Git · GitHub |
| Frontend PWA | Previsto |
| Cartografía | Prevista |

## `03` / Current progress

**Semana 1 de 4 — Base funcional**

- [ ] Configuración de base de datos y migraciones.
- [ ] Gestión editorial mediante Django Admin.
- [ ] Validación de fichas patrimoniales.
- [ ] API de lectura de bienes y categorías.
- [ ] Pruebas y evidencias documentadas.

Los elementos se marcarán cuando su implementación haya sido verificada.

## `04` / Preview

Las siguientes secciones se completarán con capturas reales del sistema.

| Evidencia | Archivo |
|---|---|
| Panel administrativo | `docs/capturas/01-panel-admin.png` |
| API de bienes | `docs/capturas/04-api-bienes.png` |
| API de categorías | `docs/capturas/05-api-categorias.png` |

## `05` / Setup

Requisitos: Python, Git y PostgreSQL configurado.

```powershell
git clone https://github.com/TU-USUARIO/paceno.git
cd paceno

py -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Configura las credenciales de la base de datos antes de ejecutar las migraciones. Si el proyecto requiere datos iniciales, ejecuta también el comando de carga definido en el código.

## `06` / Testing

```powershell
python manage.py test patrimonio
```

Los resultados y las evidencias de las pruebas se documentarán en `docs/pruebas/`. La ejecución debe verificarse antes de reportar pruebas aprobadas.

## `07` / Roadmap

- **01 — Foundation:** backend, datos, administración y API.
- **02 — Exploration:** catálogo público, mapa e interfaz adaptable.
- **03 — Interaction:** actividades educativas y reportes ciudadanos.
- **04 — Validation:** integración, pruebas y documentación final.

---

<p align="center">
  <sub>PACEÑO · SOFTWARE DEVELOPMENT PROJECT</sub><br>
  <sub>Desarrollo de Software e Innovación Tecnológica · La Paz, Bolivia</sub>
</p>
