from django.apps import AppConfig


class PatientsAppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    models = 'patients_appointments.infrastructure.db.models'
    name = 'patients_appointments'
    # container = None
    
    
    def ready(self):
        from .containers import Container
        self.container = Container()
        # self.container.wire(
        #     modules=[
        #         "patients_appointments.use_cases",
        #         "patients_appointments.presentation"
        #     ]
        # )
        self.container.wire(
            packages=[
                "patients_appointments.use_cases",
                "patients_appointments.presentation"
                
            ],
            modules=[
                "patients_appointments.presentation.views.book_appointment_view"
            ]
        )
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@22")
        print(self.container.providers)