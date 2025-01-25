from django.db import models


class Doctor(models.Model):
    """
    Doctor database model
    """
    name = models.CharField(max_length=100, blank=False)
    specialization = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=15, blank=False)


class Slot(models.Model):
    """
    Doctor availability slot data model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=5, decimal_places=3)
    time = models.DateTimeField()
