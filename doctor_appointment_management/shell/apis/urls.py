from django.urls import path
from .views import AppointmentScheduledView, AppointmentCompleteView, AppointmentCancelView

urlpatterns = [
    path('booked/', AppointmentScheduledView.as_view(), 
         name='scheduled-appointments'),
    path('<int:id>/cancel/', AppointmentCancelView.as_view(),
         name='cancel-appointment'),
    path('<int:id>/complete/', AppointmentCompleteView.as_view(),
         name='complete-appointment'),
]
