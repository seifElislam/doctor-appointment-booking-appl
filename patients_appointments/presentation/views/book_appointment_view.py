
from rest_framework.views import APIView
from dependency_injector.wiring import inject, Provide

from rest_framework.response import Response

from patients_appointments.containers import Container
from patients_appointments.presentation.exceptions.exception_handler_decorator import exception_handler_decorator
from patients_appointments.presentation.exceptions.custom_exception import CustomException

class BookAppointmentView(APIView):
    @exception_handler_decorator
    @inject
    def post(self,request,use_case = Provide[Container.book_appointment_use_case]):
        try:
            use_case.execute(request.data['patient_id'], request.data['slot_id'])
        except Exception as e:
           raise CustomException(str(e))
        
        return Response(status=201)