from doctor_appointment_management.core.outputports.appointment_management_repo_interface import \
AppointmentManagementRepoInterface
from shared.domain.event_bus_interface import EventBusInterface

class AppointmentBookedHandler:
    def __init__(self, repository: AppointmentManagementRepoInterface, event_bus: EventBusInterface):
        self.repository = repository
        self.event_bus = event_bus

    def handle_booked_appointment(self, appointment_data):
        self.repository.add_booked_appointment(appointment_data)
