
from rest_framework.views import APIView
from dependency_injector.wiring import inject, Provide

from rest_framework.response import Response

from patients_appointments.containers import Container

class BookAppointmentView(APIView):
    
    @inject
    def post(self,request,use_case = Provide[Container.book_appointment_use_case]):
        use_case.execute(request.data['patient_id'], request.data['slot_id'])
        
        return Response(status=201)