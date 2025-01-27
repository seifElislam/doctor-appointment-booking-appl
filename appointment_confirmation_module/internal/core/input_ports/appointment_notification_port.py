from abc import abstractmethod, ABC

from appointment_confirmation_module.internal.core.models.appointment_notification import AppointmentNotification


class AppointmentNotificationPort(ABC):
    @abstractmethod
    def notify(self, appointment_notification: AppointmentNotification) -> None:
        pass
