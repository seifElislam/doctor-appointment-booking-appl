from django.apps import AppConfig


class DoctorAppointmentManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor_appointment_management'

    def ready(self):
        import doctor_appointment_management.core.event_handlers.subscribtions
