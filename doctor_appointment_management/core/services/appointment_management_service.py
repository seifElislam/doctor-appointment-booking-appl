from doctor_appointment_management.core.inputports.appointment_management_service_port import \
AppointmentManagementServicePort
from doctor_appointment_management.core.outputports.appointment_management_repo_interface import \
AppointmentManagementRepoInterface


class AppointmentManagementService(AppointmentManagementServicePort):

    def __init__(self, repository: AppointmentManagementRepoInterface):
        self.repository = repository

    def get_schedeuled_appointments(self) -> list:
        return self.repository.get_schedeuled()

    def cancel_appointment(self, appointment_id: int) -> None:
        self.repository.cancel(appointment_id)

    def mark_appointment_as_completed(self, appointment_id: int) -> None:
        self.repository.complete(appointment_id)
