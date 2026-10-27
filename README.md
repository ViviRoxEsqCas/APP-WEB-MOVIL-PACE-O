# Paceño – Semana 1 (M5 base + M1 + lectura de API)

```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
django-admin startproject config .                   # en una carpeta vacía
# copiar patrimonio/ y reemplazar config/urls.py; pegar config/settings_snippet.py al final de config/settings.py
createdb paceno                                      # o crear la BD desde pgAdmin
python manage.py makemigrations patrimonio && python manage.py migrate
python manage.py seed                                # catálogos, zona piloto, grupos Editor/Administrador
python manage.py createsuperuser
python manage.py test patrimonio                     # PT-02, PT-03, PT-04, PT-21
python manage.py runserver
```
Cuentas: en /admin crear usuarios con "Es staff" marcado y asignar el grupo Editor o Administrador.
API: GET /api/bienes/ (?categoria=ID &q=texto), /api/bienes/{id}/, /api/categorias/
