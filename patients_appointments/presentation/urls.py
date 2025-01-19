from django.urls import path
from patients_appointments.presentation.views.book_appointment_view import BookAppointmentView
from patients_appointments.presentation.views.list_available_slots_view import ListAvailableSlotsView
urlpatterns = [
    path('slots', ListAvailableSlotsView.as_view(), name='list_available_slots'),
    path('book', BookAppointmentView.as_view(), name='book_appointment'),
]