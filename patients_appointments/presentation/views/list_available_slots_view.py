from rest_framework.views import APIView
from rest_framework.response import Response
from dependency_injector.wiring import Provide , inject

from patients_appointments.containers import Container
from patients_appointments.presentation.exceptions.exception_handler_decorator import exception_handler_decorator
from patients_appointments.presentation.serializers import SlotSerializer

class ListAvailableSlotsView(APIView):
    @exception_handler_decorator
    @inject
    def get(self,request,use_case = Provide[Container.list_available_appointments_use_case]):
        slots = use_case.execute(doctor_id=request.query_params['doctor_id'])
        return Response(data=SlotSerializer(slots,many=True).data)