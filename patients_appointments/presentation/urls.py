from django.urls import path
from patients_appointments.presentation.views.book_appointment_view import BookAppointmentView
urlpatterns = [
    # path('appointments/', ListAvailableAppointmentsView.as_view(), name='list_available_appointments'),
    path('book', BookAppointmentView.as_view(), name='book_appointment'),
]