from appointment_confirmation_module.core.models.appointment_notification import AppointmentNotification
from appointment_confirmation_module.core.output_ports.appointment_notification_repo_abc import AppointmentNotificationRepoAbc
from appointment_confirmation_module.shell.db.models import Notification
from appointment_confirmation_module.core.models.notification import Notification as NotificationModel


class AppointmentNotificationRepoImp(AppointmentNotificationRepoAbc):
    def save(self, notification: NotificationModel) -> None:
        self.save_appointment_notification(notification)

    def save_appointment_notification(self, notification: NotificationModel):
        Notification(
            title=notification.get_title(),
            description=notification.get_description(),
            created_at=notification.get_created_at(),
        ).save()

