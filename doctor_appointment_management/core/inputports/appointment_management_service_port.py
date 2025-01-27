from abc import ABC, abstractmethod

class AppointmentManagementServicePort(ABC):
    @abstractmethod
    def get_booked_appointments(self) -> list:
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id: int) -> None:
        pass

    @abstractmethod
    def mark_appointment_as_completed(self, appointment_id: int) -> None:
        pass
