from django.apps import AppConfig


class DoctorAvailabilityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor_availability'

    def ready(self):
        import doctor_availability.infrastructure.models
