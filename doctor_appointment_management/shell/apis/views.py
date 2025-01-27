from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from doctor_appointment_management.core.services.appointment_management_service import \
AppointmentManagementService
from doctor_appointment_management.shell.repositories.appointment_management_repository import \
AppointmentManagementRepository

class AppointmentScheduledView(APIView):
    def get(self, request):
        try:
            repository = AppointmentManagementRepository()
            service = AppointmentManagementService(repository)
            appointments = service.get_booked_appointments()
            return Response({"appointments": appointments}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AppointmentCancelView(APIView):
    def post(self, request, id=None):
        try:
            repository = AppointmentManagementRepository()
            service = AppointmentManagementService(repository)
            service.cancel_appointment(id)
            return Response({"message": "Appointment canceled successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AppointmentCompleteView(APIView):
    def post(self, request, id=None):
        try:
            repository = AppointmentManagementRepository()
            service = AppointmentManagementService(repository)
            service.mark_appointment_as_completed(id)
            return Response({"message": "Appointment completed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
