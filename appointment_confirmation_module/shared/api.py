from appointment_confirmation_module.shared.doctor_dto import DoctorDTO
from appointment_confirmation_module.shared.patient_dto import PatientDTO
from appointment_confirmation_module.shared.slot_dto import SlotDTO
from appointment_confirmation_module.shell.services.apointment_notification_adapter import AppointmentNotificationAdapter


def send_appointment_notification(doctor_dto:DoctorDTO,patient_dto:PatientDTO,slot_dto:SlotDTO):
    doctor = doctor_dto.get_doctor_domain_model()
    patient = patient_dto.get_patient_domain_model()
    slot = slot_dto.get_slot_domain_model(doctor=doctor,patient=patient)
    adapter = AppointmentNotificationAdapter()
    adapter.notify(slot)