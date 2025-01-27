from abc import ABC, abstractmethod

class AppointmentManagementRepoInterface(ABC):
    @abstractmethod
    def get_by_status(self, status: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def update_status(self, appointment_id: int, status: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_booked_appointment(self, appointment_data) -> None:
        raise NotImplementedError
