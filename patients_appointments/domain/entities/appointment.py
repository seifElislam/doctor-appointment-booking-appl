from dataclasses import dataclass
from datetime import datetime

@dataclass
class Appointment:
    patient_id: int
    slot_id: int
    reserved_at: datetime
    patient_name: str
    id: int = None
    
