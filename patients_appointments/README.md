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
```

## Features

- **List Available Appointments**: Patients can view a list of available appointments for a specific doctor.
- **Book Appointments**: Patients can book an available appointment.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd patients_appointments
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://localhost:8000/`.
- Use the provided endpoints to list and book appointments.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.