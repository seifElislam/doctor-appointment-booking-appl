from patients_appointments.domain.events.appointment_booked_event import AppointmentBookedEvent
from shared.domain.event_bus_interface import EventBusInterface
from shared.domain.event_bus_setup import event_bus

class DomainEventPublisher:
    def __init__(self, event_bus: EventBusInterface):
        self.event_bus = event_bus

    def appointment_booked_puplish(self, appointment):
        event_payload = AppointmentBookedEvent(
            id = appointment.id,
            patient_id = appointment.patient_id,
            slot_id = appointment.slot_id,
            patient_name = appointment.patient_name,
            reserved_at = appointment.reserved_at,
            status = "booked"
        )
        
        event_bus.publish("appointment_booked" ,event_payload)
