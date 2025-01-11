from dataclasses import dataclass

from appointment_confirmation_module.core.output_ports.notification_providers.notification_provider_port import NotificationProviderPort


@dataclass
class NotificationSenderService:

    providers: list[NotificationProviderPort]

    def send(self, notification):
        for provider in self.providers:
            provider.notify(notification)
        return None