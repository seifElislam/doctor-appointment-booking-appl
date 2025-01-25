# README.md for Patients Appointments Management System

# Patients Appointments Management System

This project is a Doctor/Patient Appointment Management System designed to facilitate the management of appointments from both the doctor's and patient's perspectives. This module specifically focuses on the patient side, allowing patients to view and book available appointments.

## Project Structure

```
├── apps.py
├── containers.py
├── domain
│   ├── entities
│   │   ├── appointment.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── slot.py
│   ├── exceptions
│   │   └── slot_is_reserved_exception.py
│   ├── interfaces
│   │   ├── repositories.py
│   │   └── services.py
│   └── value_objects
│       └── appointment_status.py
├── infrastructure
│   ├── db
│   │   ├── migrations
│   │   │   
│   │   └── models
│   │       ├── appointment_entity.py
│   │       └── slot_entity.py
│   ├── gateways
│   └── repositories
│       ├── appointment_repository.py
│       └── slot_repository.py
├── presentation
│   ├── serializers.py
│   ├── urls.py
│   └── views
│       └── book_appointment_view.py
├── README.md
└── use_cases
   ├── book_appointment.py
   └── list_available_appointments.py
```
