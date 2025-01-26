from typing import List, Dict
from patients_appointments.domain.exceptions.doctor_exceptions import DoctorDoesNotExistException
from patients_appointments.domain.interfaces.repositories import DoctorRepositoryInterface
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.infrastructure.db.models.doctor_entity import Doctor as DoctorEntity

class DoctorRepository(DoctorRepositoryInterface):
   
    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        try:
            doctor = DoctorEntity.objects.get(id=doctor_id)
        except DoctorEntity.DoesNotExist:
            raise DoctorDoesNotExistException(doctor_id)
        
        return doctor.to_domain()
    