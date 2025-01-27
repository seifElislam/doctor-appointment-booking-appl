from django.contrib import admin
from patients_appointments.infrastructure.db.models.appointment_entity import \
Appointment as AppointmentPatient
from patients_appointments.infrastructure.db.models.slot_entity import Slot as SlotPatient
from patients_appointments.infrastructure.db.models.doctor_entity import Doctor as DoctorPatient
from patients_appointments.infrastructure.db.models.patient_entity import Patient as PatientPatient

admin.site.register(AppointmentPatient)
admin.site.register(SlotPatient)
admin.site.register(DoctorPatient)
admin.site.register(PatientPatient)
