
from patients_appointments.domain.entities.appointment import Appointment
from patients_appointments.domain.entities.slot import Slot
from datetime import datetime
from dependency_injector.wiring import inject , Provide
from patients_appointments.domain.interfaces.repositories import AppointmentRepositoryInterface , SlotRepositoryInterface

class BookAppointmentUseCase:
    @inject
    def __init__(self,appointment_repository = Provide[AppointmentRepositoryInterface], slot_repository = Provide[SlotRepositoryInterface]):
        self.appointment_repository = appointment_repository
        # self.slot_repository = SlotRepository()
        
        self.appointment_repository = appointment_repository
        self.slot_repository = slot_repository
        
    def execute(self, patient_id: str, slot_id: int):
        print("ssssssssssssssssssssssssssss")
        # slot:Slot = self.slot_repository.get_slot_by_id(slot_id)
        
        
        appointment = Appointment(
            patient_id=patient_id,
            slot_id=1,
            reserved_at=datetime.now(),
            patient_name="patient_name"
        )
        
        # slot.mark_as_reserved()
        
        self.appointment_repository.save_appointment(appointment)
        # self.slot_repository.save_slot(slot)
        
        return None