from patients_appointments.domain.entities.appointment import Appointment as DomainAppointment
from patients_appointments.domain.interfaces.repositories import AppointmentRepositoryInterface

from patients_appointments.infrastructure.db.models.appointment_entity import Appointment


class AppointmentRepository(AppointmentRepositoryInterface):
    def get_appointment_by_id(self, appointment_id):
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            return appointment.to_domain()
        except Appointment.DoesNotExist:
            return Appointment.DoesNotExist(f"Appointment with id {appointment_id} does not exist")

    def list_appointments(self):
        return [appointment.to_domain() for appointment in Appointment.objects.all()]

    def save_appointment(self, appointment):
        django_appointment = Appointment(
            slot_id=appointment.slot_id,
            patient_id=appointment.patient_id,
            patient_name=appointment.patient_name,
            reserved_at=appointment.reserved_at
            reserved_at=appointment.reserved_at
        )
        django_appointment.save()