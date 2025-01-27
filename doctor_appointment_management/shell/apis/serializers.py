from rest_framework.serializers import ModelSerializer

from doctor_appointment_management.shell.db.appointment_entity import AppointmentManagement as AppointmentEntity


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = AppointmentEntity
        fields = ['id', 'slotId', 'patientId', 'patientName', 'reserved_at', 'status']
