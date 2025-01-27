from dataclasses import dataclass
from datetime import datetime

@dataclass
class Appointment:
    id: int
    patient_name: str
    patient_id: int
    slot_id: int
    reserved_at: datetime
    status: str = "booked"

    def get_id(self):
        return self.id

    def get_reserved_at(self):
        return self.reserved_at

    def get_status(self):
        return self.status

    def get_patient_name(self):
        return self.patientName
