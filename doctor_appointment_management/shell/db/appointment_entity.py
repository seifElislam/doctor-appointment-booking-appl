from django.db import models

class AppointmentManagement(models.Model):
    id = models.AutoField(primary_key=True)
    slot_id = models.IntegerField()
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default="booked")
