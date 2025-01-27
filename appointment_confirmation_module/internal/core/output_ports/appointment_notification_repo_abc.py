from abc import abstractmethod, ABC

from appointment_confirmation_module.internal.core.models.appointment_notification import AppointmentNotification
from appointment_confirmation_module.internal.core.models.notification import Notification


class NotificationRepoAbc(ABC):
    @abstractmethod
    def save(self, notification: Notification) -> None:
        pass
