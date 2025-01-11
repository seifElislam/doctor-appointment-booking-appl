from abc import abstractmethod, ABC

from appointment_confirmation_module.core.models.appointment_notification import AppointmentNotification


class AppointmentNotificationRepoAbc(ABC):
    @abstractmethod
    def save(self, notification: AppointmentNotification) -> None:
        pass
