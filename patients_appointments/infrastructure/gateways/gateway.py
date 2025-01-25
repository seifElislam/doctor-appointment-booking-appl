from appointment_confirmation_module.shared.doctor_dto import DoctorDTO
from appointment_confirmation_module.shared.patient_dto import PatientDTO
from appointment_confirmation_module.shared.slot_dto import SlotDTO

from appointment_confirmation_module.shared.api import send_appointment_notification
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.slot import Slot
from patients_appointments.domain.interfaces.gateways import AppointmentConfirmationGatewayInterface

class Gateway(AppointmentConfirmationGatewayInterface):
    
    def send_notification(self , patient:Patient , doctor:Doctor , slot:Slot):
        patient_dto = PatientDTO(patient.id,patient.name,patient.email,patient.phone)
        doctor_dto = DoctorDTO(doctor.id,doctor.name,doctor.email,doctor.phone)
        slot_dto = SlotDTO(slot.id,slot.time,slot.is_reserved)
        send_appointment_notification(doctor_dto,patient_dto,slot_dto)
        