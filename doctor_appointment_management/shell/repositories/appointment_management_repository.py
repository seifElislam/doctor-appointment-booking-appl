from doctor_appointment_management.core.outputports.appointment_management_repo_interface import \
AppointmentManagementRepoInterface
from doctor_appointment_management.shell.db.appointment_entity import AppointmentManagement as AppointmentEntity
from django.shortcuts import get_object_or_404

class AppointmentManagementRepository(AppointmentManagementRepoInterface):
    def get_by_status(self, status: str) -> list:
        return AppointmentEntity.objects.filter(status=status).values(
            "id", "slot_id", "patient_id", "patient_name", "reserved_at", "status")

    def update_status(self, appointment_id: int, status: str) -> None:
        appointment = get_object_or_404(AppointmentEntity, id=appointment_id)
        appointment.status = status
        appointment.save()

    def add_booked_appointment(self, appointment_data) -> None:
        AppointmentEntity.objects.create(**appointment_data)
