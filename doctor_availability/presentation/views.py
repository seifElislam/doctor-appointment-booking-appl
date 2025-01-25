"""
Doctor availability views
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from doctor_availability.application.services import list_doctors, add_doctor, list_doctor_avail_slots, add_slot, \
    get_doctor_by_id
from doctor_availability.application.serializers import DoctorSerializer, SlotSerializer


class DoctorAPIView(APIView):
    def get(self, request):
        # Get all objects
        objects = list_doctors()
        serializer = DoctorSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new object
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            add_doctor(serializer.to_dto())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlotAPIView(APIView):
    def get(self, request):
        doctor_id = request.query_params.get('doctor_id', None)
        if doctor_id:
            objects = list_doctor_avail_slots(doctor_id)
            serializer = SlotSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # Create a new object
        serializer = SlotSerializer(data=request.data)
        if serializer.is_valid():
            doctor_obj = get_doctor_by_id(request.data['doctor_id'])
            slot_obj = add_slot(serializer.to_dto(), doctor_obj)
            return Response(slot_obj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
