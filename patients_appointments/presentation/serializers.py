from rest_framework import serializers
from patients_appointments.infrastructure.db.models.appointment_entity import Appointment
from patients_appointments.infrastructure.db.models.slot_entity import Slot

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor_id', 'patient_id', 'time', 'is_reserved']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'doctor_id', 'time', 'is_reserved']
    
    