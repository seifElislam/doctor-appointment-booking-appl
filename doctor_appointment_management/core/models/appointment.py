from dataclasses import dataclass
from doctor_appointment_management.core.models.patient import Patient
from datetime import datetime
# import uuid

@dataclass
class Appointment:
    id: int
    patient: Patient
    reserved_at: datetime
    status: str = "scheduled"

    def get_id(self):
        return self.id

    def get_reserved_at(self):
        return self.reserved_at

    def get_status(self):
        return self.status
