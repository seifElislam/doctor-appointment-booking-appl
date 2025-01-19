from rest_framework import serializers
from patients_appointments.infrastructure.db.models.appointment_entity import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor_id', 'patient_id', 'date', 'time', 'status']