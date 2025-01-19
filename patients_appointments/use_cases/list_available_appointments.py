def list_available_appointments(doctor_id):
    """
    List available appointments for a specific doctor.

    Args:
        doctor_id (int): The ID of the doctor for whom to list available appointments.

    Returns:
        list: A list of available appointments for the specified doctor.
    """
    from patients_appointments.domain.interfaces.repositories import AppointmentRepository

    repository = AppointmentRepository()
    available_appointments = repository.list_appointments(doctor_id=doctor_id, status='AVAILABLE')
    
    return available_appointments