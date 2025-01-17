from django.urls import path
from .views import AppointmentScheduledView, AppointmentCompleteView, AppointmentCancelView

urlpatterns = [
    path('appointments/', AppointmentScheduledView.as_view(), 
         name='scheduled-appointments'),
    path('appointment/<int:id>/cancel/', AppointmentCancelView.as_view(),
         name='cancel-appointment'),
    path('appointment/<int:id>/complete/', AppointmentCompleteView.as_view(),
         name='complete-appointment'),
]
