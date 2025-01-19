# README.md for Patients Appointments Management System

# Patients Appointments Management System

This project is a Doctor/Patient Appointment Management System designed to facilitate the management of appointments from both the doctor's and patient's perspectives. This module specifically focuses on the patient side, allowing patients to view and book available appointments.

## Project Structure

```
patients_appointments
├── domain
│   ├── entities
│   ├── interfaces
│   └── value_objects
├── infrastructure
│   ├── models.py
│   ├── repositories
│   └── serializers.py
├── presentation
│   ├── urls.py
│   └── views.py
├── use_cases
│   ├── list_available_appointments.py
│   └── book_appointment.py
├── apps.py
└── README.md
