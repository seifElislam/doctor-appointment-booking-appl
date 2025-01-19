from patients_appointments.domain.entities.appointment import Appointment
from patients_appointments.domain.entities.slot import Slot

class AppointmentRepositoryInterface:
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        pass

    def list_appointments(self, doctor_id: int):
        pass

    def save_appointment(self, appointment: Appointment):
        pass
    

class SlotRepositoryInterface:
    def get_slot_by_id(self, slot_id: int)-> Slot:
        pass

    def list_slots(self, doctor_id: int):
        pass
    
    def list_available_slots(self, doctor_id: int):
        pass

    def save_slot(self, slot: Slot):
        pass