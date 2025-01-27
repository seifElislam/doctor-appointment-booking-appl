from appointment_confirmation_module.internal.core.output_ports.notification_providers.simple_notification_provider_port import \
    SimpleNotificationProviderPort


class SimpleNotificationProvider(SimpleNotificationProviderPort):
    def notify(self, notification):
        print(f"Sending notification: {notification}")
        return None