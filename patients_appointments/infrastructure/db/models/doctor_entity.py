from django.db import models
from patients_appointments.domain.entities.doctor import Doctor as DomainDoctor
class Doctor(models.Model):
    """
    Unmanaged Doctor entity that maps to existing doctors table
    """
    name = models.CharField(max_length=100, db_column='name')
    specialization = models.CharField(max_length=100, db_column='specialization')
    email = models.EmailField(max_length=100, db_column='email')
    phone = models.CharField(max_length=15, db_column='phone')

    class Meta:
        managed = False
        db_table = 'doctor_availability_doctor'  # Django's default table name pattern
    
    
    def to_domain(self):
        return DomainDoctor(
            id=self.id,
            name=self.name,
            email=self.email,
            phone=self.phone
        )