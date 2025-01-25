from django.db import models
from patients_appointments.domain.entities.slot import Slot as DomainSlot

class Slot(models.Model):
    time = models.DateTimeField()
    doctor_id = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cost = models.DecimalField(max_digits=5, decimal_places=3)
    
    class Meta:
        managed = False # this model is managed by another module 
        db_table = 'doctor_availability_slot'
    
    def to_domain(self):
        return DomainSlot(
            id=self.id,
            time=self.time,
            doctor_id=self.doctor_id,
            is_reserved=self.is_reserved
        )