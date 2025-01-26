from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients_appointments/', include('patients_appointments.presentation.urls')),
    path('api/doctor-avail/', include('doctor_availability.presentation.urls'))
    path('api/v1/appointment-management/', include('doctor_appointment_management.shell.apis.urls')),
]
