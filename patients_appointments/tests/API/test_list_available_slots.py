from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from patients_appointments.infrastructure.db.models.slot_entity import Slot as SlotModel


class TestListAvailableSlots(APITestCase):
    
    
    def test_list_available_slots_success(self):
        #arrange
        slot1 = SlotModel.objects.create(
            time='2024-01-01 10:00:00',
            doctor_id=1,
            doctor_name="Dr. Smith",
            is_reserved=False
        )
        slot2 = SlotModel.objects.create(
            time='2024-01-01 11:00:00',
            doctor_id=1,
            doctor_name="Dr. Smith",
            is_reserved=False
        )
        reversed_slot = SlotModel.objects.create(
            time='2024-01-01 12:00:00',
            doctor_id=1,
            doctor_name="Dr. Smith",
            is_reserved=True
        )
        #act
        url = reverse('list-available-slots')
        response = self.client.get(url, {'doctor_id': 1})
        #assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], slot1.id)
        self.assertEqual(response.data[1]['id'], slot2.id)
    
  
    
    def test_list_available_slots_no_slots(self):
        resrved_slot_1 = SlotModel.objects.create(
            time='2024-01-01 10:00:00',
            doctor_id=1,
            doctor_name='Dr. Smith',
            is_reserved=True
        )
        resrved_slot_2 = SlotModel.objects.create(
            time='2024-01-01 11:00:00',
            doctor_id=1,
            doctor_name='Dr. Smith',
            is_reserved=True
        )
        url = reverse('list-available-slots')
        response = self.client.get(url, {'doctor_id': 1})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
