from django.apps import AppConfig


class SharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared'

    def ready(self):
        from .domain.event_bus_setup import event_bus
