from dataclasses import dataclass
from datetime import datetime

from appointment_confirmation_module.core.models.slot import Slot


@dataclass
class SlotDTO:
    date: datetime


    def get_date(self) -> datetime:
        return self.date

    def get_slot_domain_model(self, doctor, patient) -> 'Slot':
        return Slot(doctor, patient, self.date)