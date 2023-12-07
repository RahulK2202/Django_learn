# apps.py

from django.apps import AppConfig


class YourAppConfig(AppConfig):
    name = 'Modelevents'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import Modelevents.signals
