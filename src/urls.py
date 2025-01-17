from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/management/', include('doctor_appointment_management.shell.apis.urls')),
]
