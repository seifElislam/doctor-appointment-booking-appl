from django.contrib import admin
from .shell.db.appointment_entity import Appointment as AppointmentEntity

admin.site.register(AppointmentEntity)
