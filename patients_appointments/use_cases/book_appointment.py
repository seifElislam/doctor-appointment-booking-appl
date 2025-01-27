
from patients_appointments.domain.entities.appointment import Appointment
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.slot import Slot
from datetime import datetime
from dependency_injector.wiring import inject , Provide
from patients_appointments.domain.interfaces.gateways import AppointmentConfirmationGatewayInterface
from patients_appointments.domain.interfaces.repositories import AppointmentRepositoryInterface, PatientRepositoryInterface , SlotRepositoryInterface , DoctorRepositoryInterface
from patients_appointments.domain.events.domain_event_puplisher import DomainEventPublisher
from shared.domain.event_bus_setup import event_bus

class BookAppointmentUseCase:
    @inject
    def __init__(self,appointment_repository = Provide[AppointmentRepositoryInterface], 
                 slot_repository = Provide[SlotRepositoryInterface] , patient_repository = Provide[PatientRepositoryInterface], doctor_repository = Provide[DoctorRepositoryInterface],
                 gateway = Provide[AppointmentConfirmationGatewayInterface]):
        
        self.appointment_repository:AppointmentRepositoryInterface = appointment_repository
        self.slot_repository:SlotRepositoryInterface = slot_repository
        self.patient_repository:PatientRepositoryInterface = patient_repository
        self.doctor_repository:DoctorRepositoryInterface= doctor_repository
        
        self.gateway:AppointmentConfirmationGatewayInterface = gateway
        
    def execute(self, patient_id: str, slot_id: int):
        slot:Slot = self.slot_repository.get_slot_by_id(slot_id)
        patient: Patient = self.patient_repository.get_patient_by_id(patient_id)
        doctor:Doctor = self.doctor_repository.get_doctor_by_id(slot.doctor_id)
        
        appointment = Appointment(
            patient_id=patient_id,
            slot_id=slot_id,
            reserved_at=datetime.now(),
            patient_name="patient_name"
        )
        
        slot.mark_as_reserved()
        
        self.appointment_repository.save_appointment(appointment)
        self.slot_repository.save_slot(slot)
        

        event_publisher = DomainEventPublisher(event_bus)
        event_publisher.appointment_booked_puplish(appointment)
        self.gateway.send_notification(slot=slot , patient= patient , doctor=doctor) # todo send confirmation notification to patient and doctor
        
        
        return None
