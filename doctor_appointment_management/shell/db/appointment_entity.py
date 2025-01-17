from django.db import models

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    # patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="scheduled")
