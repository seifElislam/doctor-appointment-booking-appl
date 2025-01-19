from datetime import datetime
from dataclasses import dataclass
from patients_appointments.domain.exceptions.slot_is_reserved_exception import SlotIsReservedException

@dataclass
class Slot:
    id: str
    time: datetime
    doctor_id: str
    doctor_name: str
    is_reserved: bool
    
    
    def mark_as_reserved(self):
        if self.is_reserved:
            raise SlotIsReservedException()
        
        self.is_reserved = True
