from django.db import models
from patients_appointments.domain.entities.slot import Slot as DomainSlot

class Slot(models.Model):
    time = models.DateTimeField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    is_reserved = models.BooleanField(default=False)
    
    # class Meta:
    #     managed = True # this model is managed by another module 
    
    def to_domain(self):
        return DomainSlot(
            id=self.id,
            time=self.time,
            doctor_id=self.doctor_id,
            doctor_name=self.doctor_name,
            is_reserved=self.is_reserved
        )