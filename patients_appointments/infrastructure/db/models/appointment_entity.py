
from django.db import models
from patients_appointments.domain.entities.appointment import Appointment as DomainAppointment


class Appointment(models.Model):
    slot_id = models.IntegerField()
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    reserved_at = models.DateField()
    

    def to_domain(self):
        return DomainAppointment(
            id=self.id,
            slot_id=self.slot_id,
            patient_id=self.patient_id,
            patient_name=self.patient_name,
            reserved_at=self.reserved_at
        )