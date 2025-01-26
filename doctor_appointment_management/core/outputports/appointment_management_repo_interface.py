from abc import ABC, abstractmethod

class AppointmentManagementRepoInterface(ABC):
    @abstractmethod
    def get_schedeuled(self) -> list:
        pass

    @abstractmethod
    def cancel(self, appointment_id: int) -> None:
        pass

    @abstractmethod
    def complete(self, appointment_id: int) -> None:
        pass
