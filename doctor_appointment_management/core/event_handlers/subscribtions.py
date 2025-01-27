from shared.domain.event_bus_setup import event_bus
from doctor_appointment_management.shell.repositories.appointment_management_repository import \
AppointmentManagementRepository
from doctor_appointment_management.core.event_handlers.appointment_booked_handler import \
AppointmentBookedHandler

repository = AppointmentManagementRepository()
handler = AppointmentBookedHandler(repository, event_bus)
event_bus.subscribe("appointment_booked", handler.handle_booked_appointment)

# def appointment_booked_event_subscribtion() -> None:
#     repository = AppointmentManagementRepository()
#     handler = AppointmentBookedHandler(repository, event_bus)
#     event_bus.subscribe("appointment.booked", handler)
