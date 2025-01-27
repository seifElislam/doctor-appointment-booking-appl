from abc import ABC, abstractmethod

from appointment_confirmation_module.internal.core.models.notification import Notification
from appointment_confirmation_module.internal.core.output_ports.notification_providers.notification_provider_port import NotificationProviderPort


class SimpleNotificationProviderPort(NotificationProviderPort):
    @abstractmethod
    def notify(self, notification: Notification) -> None:
        pass