from abc import abstractmethod, ABC

from appointment_confirmation_module.core.models.appointment_notification import AppointmentNotification
from appointment_confirmation_module.core.models.notification import Notification


class AppointmentNotificationRepoAbc(ABC):
    @abstractmethod
    def save(self, notification: Notification) -> None:
        pass
