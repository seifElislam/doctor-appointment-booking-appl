from abc import ABC, abstractmethod

from appointment_confirmation_module.internal.core.models.notification import Notification


class NotificationProviderPort(ABC):
    @abstractmethod
    def notify(self, notification:Notification) -> None:
        pass