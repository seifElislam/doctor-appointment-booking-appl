from django.apps import AppConfig


class AppointmentConfirmationModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment_confirmation_module'
    models_module = 'appointment_confirmation_module.shell.db.models'
    # migrations_module = 'appointment_confirmation_module.shell.db.migrations'