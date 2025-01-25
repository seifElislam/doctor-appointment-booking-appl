from django.db import models
from patients_appointments.domain.entities.patient import Patient as DomainPatient

class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def to_domain(self):
        return DomainPatient(
            id=self.id,
            name=self.name,
            email=self.email,
            phone=self.phone
        )