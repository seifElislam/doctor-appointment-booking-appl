from abc import ABC, abstractmethod

from appointment_confirmation_module.core.models.notification import Notification


class SimpleNotificationProviderPort(ABC):
    @abstractmethod
    def notify(self, notification: Notification) -> None:
        pass