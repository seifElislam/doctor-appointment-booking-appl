from django.contrib import admin
from .shell.db.appointment_entity import AppointmentManagement as AppointmentEntity

admin.site.register(AppointmentEntity)
