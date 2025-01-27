from typing import TypedDict
from datetime import datetime

class AppointmentBookedEvent(TypedDict):
    id: int
    patient_name: str
    patient_id: int
    slot_id: int
    reserved_at: datetime
    status: str = "booked"
