# Generated by Django 4.2 on 2025-01-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('patient_name', models.CharField(max_length=255)),
                ('reserved_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('doctor_id', models.IntegerField()),
                ('doctor_name', models.CharField(max_length=255)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
