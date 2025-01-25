from typing import List, Dict
from patients_appointments.domain.interfaces.repositories import DoctorRepositoryInterface
from patients_appointments.domain.entities.doctor import Doctor

class InMemoryDoctorRepository(DoctorRepositoryInterface):
    def __init__(self):
        self._doctors: Dict[int, Doctor] = {}
        self._doctors[1] = Doctor(id=1, name="Dr. John Doe", email="john@example.com", phone="1234567890")
        
    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        doctor = self._doctors.get(doctor_id)
        if doctor is None:
            raise ValueError(f"Doctor with id {doctor_id} not found")
        return doctor

    