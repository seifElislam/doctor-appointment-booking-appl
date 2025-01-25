"""

"""
from rest_framework import serializers
from doctor_availability.infrastructure.models import Doctor, Slot
from doctor_availability.application import dto


class DoctorSerializer(serializers.ModelSerializer):
    """
    Doctor model serializer class
    """

    class Meta:
        model = Doctor

    def to_dto(self):
        return dto.Doctor(
            id=self.validated_data['id'],
            name=self.validated_data['name'],
            specialization = self.validated_data['specialization']
        )


class SlotSerializer(serializers.ModelSerializer):
    """
    Doctor model serializer class
    """

    class Meta:
        model = Slot

    def to_dto(self):
        return dto.Slot(
            id=self.validated_data['id'],
            doctor_id=self.validated_data['doctor_id'],
            is_reserved=self.validated_data['is_reserved'],
            cost=self.validated_data['cost']
        )
