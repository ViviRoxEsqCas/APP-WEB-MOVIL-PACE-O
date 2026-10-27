# PACEÑO — Semana 1
> **Base funcional:** Gestión patrimonial, administración y API de lectura.

---

## 1. Descripción del proyecto

**PACEÑO** es una aplicación web móvil orientada a la difusión y valoración del patrimonio cultural del municipio de La Paz, Bolivia.

El proyecto propone integrar un catálogo patrimonial documentado, exploración geográfica, actividades educativas y reportes ciudadanos en una plataforma web progresiva (PWA).

Durante la primera semana, el desarrollo se concentra en la estructura del backend, la gestión de bienes patrimoniales, el control de acceso editorial y los endpoints de lectura.

---

## 2. Objetivo de la semana 1

Implementar una base funcional que permita administrar fichas patrimoniales, validar los datos necesarios para su publicación y consultar los bienes publicados mediante una API.

### Entregables previstos
* [x] Proyecto Django y dependencias configuradas.
* [x] Base de datos PostgreSQL y migraciones aplicables.
* [x] Panel Django Admin con grupos **Editor** y **Administrador**.
* [x] Modelos y validaciones para la gestión patrimonial.
* [x] Endpoints de lectura de bienes y categorías.
* [x] Entre 5 y 8 fichas patrimoniales iniciales.
* [x] Evidencias del panel, la API y las pruebas funcionales.

---

## 3. Tecnologías

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python y Django |
| **API REST** | Django REST Framework |
| **Base de datos** | PostgreSQL |
| **Administración** | Django Admin |
| **Control de versiones** | Git y GitHub |
| **Frontend PWA** | React y Vite *(previstos para la semana 2)* |
| **Mapa** | Leaflet *(previsto para la semana 2)* |

> *La configuración definitiva de cada componente debe corresponder al código disponible en el repositorio.*

---

## 4. Estructura del proyecto

```text
PACEÑO/
├── config/
├── patrimonio/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    ├── capturas/
    └── pruebas/
```

> **Nota:** El entorno virtual `venv/` se utiliza localmente y está excluido del repositorio.

---

## 5. Requisitos previos

* Python 3.x instalado.
* Git instalado.
* PostgreSQL instalado y accesible.
* Una base de datos creada para el proyecto.

---

## 6. Instalación en Windows

### 6.1. Clonar el repositorio
```powershell
git clone https://github.com/TU-USUARIO/paceno.git
cd paceno
```
*(Sustituir `TU-USUARIO` por el usuario correspondiente de GitHub).*

### 6.2. Crear y activar el entorno virtual
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```
*(Si ya existe un entorno virtual funcional, se puede activar en lugar de crearlo nuevamente).*

### 6.3. Instalar dependencias
```powershell
python -m pip install -r requirements.txt
```

### 6.4. Configurar la base de datos
1. Crear una base de datos llamada `paceno` desde PostgreSQL o pgAdmin.
2. Verificar que los parámetros de conexión estén configurados en Django. Las credenciales deben mantenerse fuera del repositorio.

### 6.5. Aplicar migraciones
```powershell
python manage.py makemigrations patrimonio
python manage.py migrate
```

### 6.6. Cargar los datos iniciales
```powershell
python manage.py seed
```
*(Este comando crea los catálogos, la zona piloto y los grupos editoriales configurados).*

### 6.7. Crear una cuenta administrativa
```powershell
python manage.py createsuperuser
```

### 6.8. Ejecutar el servidor
```powershell
python manage.py runserver
```

**Panel administrativo:**
👉 `http://127.0.0.1:8000/admin/`

---

## 7. Roles y administración

El sistema contempla dos grupos editoriales:

* **Editor:** Administra fichas patrimoniales según los permisos asignados, sin acceso a la gestión de usuarios.
* **Administrador:** Dispone de todos los permisos de administración definidos para el sistema.

### Procedimiento de asignación
Para asignar un grupo:
1. Ingresar al panel administrativo (`/admin/`).
2. Crear o editar un usuario.
3. Marcar la opción de acceso al sitio administrativo (*es staff / acceso al sitio administrativo*).
4. Seleccionar el grupo adecuado (**Editor** o **Administrador**).

> *Los permisos deben verificarse mediante pruebas con cuentas de ambos roles.*

---

## 8. API de lectura

Endpoints previstos para la consulta pública de bienes y categorías:

| Método | Endpoint | Función |
| :---: | :--- | :--- |
| `GET` | `/api/bienes/` | Listar bienes publicados |
| `GET` | `/api/bienes/{id}/` | Consultar el detalle de un bien |
| `GET` | `/api/categorias/` | Consultar categorías |

### Parámetros de consulta para el listado:
* `categoria`: Filtrar por identificador de categoría.
* `q`: Buscar por texto.

#### Ejemplos de uso:
* **Listado general:** `http://127.0.0.1:8000/api/bienes/`
* **Con filtros:** `http://127.0.0.1:8000/api/bienes/?categoria=1&q=plaza`

> **Regla de negocio:** Los bienes que no estén en estado **`publicado`** no aparecerán en el listado público.

---

## 9. Evidencias de la semana 1

Las capturas se almacenan en `docs/capturas/` y los registros de pruebas en `docs/pruebas/`.

### Capturas requeridas

| Archivo | Evidencia |
| :--- | :--- |
| `01-panel-admin.png` | Panel Django Admin en funcionamiento |
| `02-grupos-editor-admin.png` | Grupos Editor y Administrador |
| `03-editor-permisos.png` | Usuario Editor sin acceso a gestión de usuarios |
| `04-api-bienes.png` | Respuesta real de `GET /api/bienes/` |
| `05-api-categorias.png` | Respuesta real de `GET /api/categorias/` |
| `06-fichas-patrimoniales.png` | Fichas iniciales registradas en el panel |

### Muestra de evidencias

![Panel administrativo](docs/capturas/01-panel-admin.png)

![API de bienes](docs/capturas/04-api-bienes.png)

---

## 10. Pruebas de validación

Casos contemplados para la primera semana:

| Código | Prueba | Resultado esperado |
| :---: | :--- | :--- |
| **PT-01** | Registro de ficha | La ficha incompleta permanece en borrador y no aparece en la API pública. |
| **PT-02** | Validación de fuente | Se rechaza la publicación sin fuente documental. |
| **PT-03** | Validación de ubicación | Se rechaza un bien material sin coordenadas o fuera del área piloto. |
| **PT-04** | Publicación de ficha | La ficha completa publicada aparece en la API. |
| **PT-05** | Imagen y licencia | Se rechaza una imagen sin autor o licencia. |
| **PT-21** | Control de acceso | El Editor no accede a la gestión de usuarios y el acceso sin sesión se restringe. |

### Ejecución de pruebas automatizadas

```powershell
python manage.py test patrimonio
```

> **Registro de resultados:** Se almacena en `docs/pruebas/semana-1.md`. Cada prueba registra código, fecha, pasos, resultado esperado/obtenido, estado (aprobada/fallida) y evidencia.

---

## 11. Estado del proyecto

* **Etapa actual:** Semana 1 de 4 — *Estructura y base funcional.*

---

## 12. Plan de trabajo

- [x] **Semana 1:** Backend, base de datos, administración editorial, validaciones y API inicial.
- [ ] **Semana 2:** Catálogo público, ficha de detalle, mapa y diseño adaptable.
- [ ] **Semana 3:** Actividades educativas y reportes ciudadanos.
- [ ] **Semana 4:** Integración, correcciones, pruebas finales y documentación.

---

## 13. Autora

**Vivian Roxana Esquivel Castillo**  
*Proyecto académico individual — Desarrollo de Software e Innovación Tecnológica.*  
La Paz, Bolivia.