# Generated by Django 4.2 on 2025-01-27 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointment_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentmanagement',
            old_name='patientId',
            new_name='patient_id',
        ),
        migrations.RenameField(
            model_name='appointmentmanagement',
            old_name='slotId',
            new_name='slot_id',
        ),
    ]
