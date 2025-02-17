from datetime import datetime
from dataclasses import dataclass
from patients_appointments.domain.exceptions.slot_exceptions import SlotIsReservedException

@dataclass
class Slot:
    id: str
    time: datetime
    doctor_id: str
    is_reserved: bool
    
    
    def mark_as_reserved(self):
        if self.is_reserved:
            raise SlotIsReservedException()
        
        self.is_reserved = True
