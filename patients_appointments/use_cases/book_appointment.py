
from patients_appointments.domain.entities.appointment import Appointment
from patients_appointments.domain.entities.slot import Slot
from datetime import datetime
from dependency_injector.wiring import inject , Provide
from patients_appointments.domain.interfaces.repositories import AppointmentRepositoryInterface , SlotRepositoryInterface
from patients_appointments.infrastructure.gateways.gateway import Gateway

class BookAppointmentUseCase:
    @inject
    def __init__(self,appointment_repository = Provide[AppointmentRepositoryInterface], 
                 slot_repository = Provide[SlotRepositoryInterface] , 
                 gateway = Provide[Gateway]):
        self.appointment_repository = appointment_repository
        self.slot_repository = slot_repository
        
        self.appointment_repository = appointment_repository
        self.slot_repository = slot_repository
        
    def execute(self, patient_id: str, slot_id: int):
        slot:Slot = self.slot_repository.get_slot_by_id(slot_id)
        
        
        appointment = Appointment(
            patient_id=patient_id,
            slot_id=slot_id,
            reserved_at=datetime.now(),
            patient_name="patient_name"
        )
        
        slot.mark_as_reserved()
        
        self.appointment_repository.save_appointment(appointment)
        self.slot_repository.save_slot(slot)
        
        #self.gateway.send_notification() # todo send confirmation notification to patient and doctor
        
        
        return None