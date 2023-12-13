from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'old.db.models.BigAutoField'
    name = 'main'
