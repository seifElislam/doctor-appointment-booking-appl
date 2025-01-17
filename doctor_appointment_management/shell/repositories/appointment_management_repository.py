from doctor_appointment_management.core.outputports.appointment_management_repo_interface import \
AppointmentManagementRepoInterface
from doctor_appointment_management.shell.db.appointment_entity import Appointment as AppointmentEntity
from django.shortcuts import get_object_or_404

class AppointmentManagementRepository(AppointmentManagementRepoInterface):
    def get_schedeuled(self) -> list:
        return AppointmentEntity.objects.filter(status="scheduled").values("id", "reserved_at", "status")

    def cancel(self, appointment_id: int):
        appointment = get_object_or_404(AppointmentEntity, id=appointment_id)
        appointment.delete()

    def complete(self, appointment_id: int):
        appointment = get_object_or_404(AppointmentEntity, id=appointment_id)
        appointment.status = "completed"
        appointment.save()
