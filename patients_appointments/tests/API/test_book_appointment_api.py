from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse
from patients_appointments.domain.entities.slot import Slot
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.domain.exceptions.slot_exceptions import SlotIsReservedException
from django.test import TransactionTestCase
from patients_appointments.infrastructure.db.models.appointment_entity import  Appointment as AppointmentModel
from patients_appointments.infrastructure.db.models.slot_entity import Slot as SlotModel
from patients_appointments.infrastructure.db.models.patient_entity import Patient as PatientModel
from patients_appointments.infrastructure.db.models.doctor_entity import Doctor as DoctorModel

class TestBookAppointmentEndToEnd(TransactionTestCase):
    def setUp(self):
        self.patient = PatientModel.objects.create( name='John Doe')
        self.doctor = DoctorModel.objects.create(name='Dr. Smith' ,specialization = 'Dentist')
        self.slot = SlotModel.objects.create(
            time='2024-01-01 10:00:00',
            doctor_id=self.doctor.id,
            cost = 10,
            is_reserved=False
        )
        self.resrved_slot = SlotModel.objects.create(
            time='2024-01-01 11:00:00',
            doctor_id=self.doctor.id,
            cost = 10,
            is_reserved=True
        )

    def test_book_appointment_end_to_end(self):
        url = reverse('book-appointment')
        data = {
            'patient_id': self.patient.id,
            'slot_id': self.slot.id
        }
        
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(SlotModel.objects.get(id=self.slot.id).is_reserved)
        self.assertTrue(AppointmentModel.objects.filter(
            patient_id=self.patient.id,
            slot_id=self.slot.id
        ).exists())
        
        
    def test_book_appointment_end_to_end_slot_is_reserved(self):
        
        url = reverse('book-appointment')
        data = {
            'patient_id': self.patient.id,
            'slot_id': self.resrved_slot.id
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(SlotModel.objects.get(id=self.resrved_slot.id).is_reserved)
        self.assertFalse(AppointmentModel.objects.filter(
            patient_id=self.patient.id,
            slot_id=self.slot.id
        ).exists())