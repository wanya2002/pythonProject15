from django.apps import AppConfig


class FirstConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'


class CatalogConfig:
    pass