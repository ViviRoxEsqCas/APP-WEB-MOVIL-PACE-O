# Pegar al FINAL de config/settings.py (generado por startproject) y ajustar INSTALLED_APPS/MIDDLEWARE.
import os

INSTALLED_APPS += ["rest_framework", "corsheaders", "patrimonio"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

DATABASES = {"default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.getenv("DB_NAME", "paceno"), "USER": os.getenv("DB_USER", "postgres"),
    "PASSWORD": os.getenv("DB_PASSWORD", ""), "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", "5432")}}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],  # API pública solo de lectura
}
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]  # origen de la PWA (Vite)
LANGUAGE_CODE, TIME_ZONE = "es", "America/La_Paz"
MEDIA_URL, MEDIA_ROOT = "/media/", BASE_DIR / "media"
