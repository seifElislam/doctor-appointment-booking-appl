from doctor_appointment_management.core.inputports.appointment_management_service_port import \
AppointmentManagementServicePort
from doctor_appointment_management.core.outputports.appointment_management_repo_interface import \
AppointmentManagementRepoInterface


class AppointmentManagementService(AppointmentManagementServicePort):

    def __init__(self, repository: AppointmentManagementRepoInterface):
        self.repository = repository

    def get_booked_appointments(self) -> list:
        return self.repository.get_by_status("booked")

    def cancel_appointment(self, appointment_id: int) -> None:
        self.repository.update_status(appointment_id, "cancelled")

    def mark_appointment_as_completed(self, appointment_id: int) -> None:
        self.repository.update_status(appointment_id, "completed")
