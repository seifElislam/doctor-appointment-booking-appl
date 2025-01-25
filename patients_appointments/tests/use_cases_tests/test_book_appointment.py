import unittest
from unittest.mock import Mock, patch
from datetime import datetime
from patients_appointments.domain.exceptions.slot_exceptions import SlotIsReservedException
from patients_appointments.use_cases.book_appointment import BookAppointmentUseCase
from patients_appointments.domain.entities.slot import Slot
from patients_appointments.domain.entities.patient import Patient
from patients_appointments.domain.entities.doctor import Doctor
from patients_appointments.domain.entities.appointment import Appointment

class TestBookAppointmentUseCase(unittest.TestCase):

    def setUp(self):
        self.appointment_repository = Mock()
        self.slot_repository = Mock()
        self.patient_repository = Mock()
        self.doctor_repository = Mock()
        self.gateway = Mock()
        
        self.use_case = BookAppointmentUseCase(
            appointment_repository=self.appointment_repository,
            slot_repository=self.slot_repository,
            patient_repository=self.patient_repository,
            doctor_repository=self.doctor_repository,
            gateway=self.gateway
        )

    def test_execute_books_appointment_successfully(self):
        # Arrange
        patient_id = "patient123"
        slot_id = 1
        
        mock_slot = Mock(spec=Slot)
        mock_slot.doctor_id = "doctor123"
        self.slot_repository.get_slot_by_id.return_value = mock_slot
        
        mock_patient = Mock(spec=Patient)
        self.patient_repository.get_patient_by_id.return_value = mock_patient
        
        mock_doctor = Mock(spec=Doctor)
        self.doctor_repository.get_doctor_by_id.return_value = mock_doctor

        # Act
        self.use_case.execute(patient_id, slot_id)

        # Assert
        self.slot_repository.get_slot_by_id.assert_called_once_with(slot_id)
        self.patient_repository.get_patient_by_id.assert_called_once_with(patient_id)
        self.doctor_repository.get_doctor_by_id.assert_called_once_with(mock_slot.doctor_id)
        
        mock_slot.mark_as_reserved.assert_called_once()
        self.appointment_repository.save_appointment.assert_called_once()
        self.slot_repository.save_slot.assert_called_once_with(mock_slot)
        self.gateway.send_notification.assert_called_once_with(
            slot=mock_slot,
            patient=mock_patient,
            doctor=mock_doctor
        )
    def test_execute_fails_when_slot_already_reserved(self):
        # Arrange
        patient_id = "patient123"
        slot_id = 1
        
        mock_slot = Slot(id=slot_id, time=datetime.now() , doctor_id="doctor123", doctor_name="Doctor Name", is_reserved=True)
        
        
        self.slot_repository.get_slot_by_id.return_value = mock_slot
        
        mock_patient = Mock(spec=Patient)
        self.patient_repository.get_patient_by_id.return_value = mock_patient
        
        # Act & Assert
        with self.assertRaises(SlotIsReservedException):
            self.use_case.execute(patient_id, slot_id)
    