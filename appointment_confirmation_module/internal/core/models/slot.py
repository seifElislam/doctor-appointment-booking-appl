from dataclasses import dataclass
from datetime import datetime

from appointment_confirmation_module.internal.core.models.doctor import Doctor
from appointment_confirmation_module.internal.core.models.patient import Patient


@dataclass
class Slot:
    doctor: Doctor
    patient: Patient
    date: datetime

    def get_doctor(self) -> Doctor:
        return self.doctor
    def get_patient(self) -> Patient:
        return self.patient
    def get_date(self) -> datetime:
        return self.date
