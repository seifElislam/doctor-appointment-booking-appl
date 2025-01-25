from abc import ABC, abstractmethod
from patients_appointments.domain.entities.appointment import Appointment
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.slot import Slot

class AppointmentRepositoryInterface(ABC):
    @abstractmethod
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        pass

    @abstractmethod
    def list_appointments(self, doctor_id: int):
        pass

    @abstractmethod
    def save_appointment(self, appointment: Appointment):
        pass
    

class SlotRepositoryInterface(ABC):
    @abstractmethod
    def get_slot_by_id(self, slot_id: int)-> Slot:
        pass

    @abstractmethod
    def list_slots(self, doctor_id: int):
        pass
    
    @abstractmethod
    def list_available_slots(self, doctor_id: int):
        pass

    @abstractmethod
    def save_slot(self, slot: Slot):
        pass
    

class PatientRepositoryInterface(ABC):
    @abstractmethod
    def get_patient_by_id(self, patient_id: int) -> Patient:
        pass

    @abstractmethod
    def list_patients(self) -> list[Patient]:
        pass

    @abstractmethod
    def save_patient(self, patient) -> Patient:
        pass

class DoctorRepositoryInterface(ABC):
    @abstractmethod
    def get_doctor_by_id(self, doctor_id: int):
        pass
