from abc import ABC, abstractmethod
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.slot import Slot

class AppointmentConfirmationGatewayInterface(ABC):
    @abstractmethod
    def send_notification(self, patient: Patient, doctor: Doctor, slot: Slot) -> None:
        pass