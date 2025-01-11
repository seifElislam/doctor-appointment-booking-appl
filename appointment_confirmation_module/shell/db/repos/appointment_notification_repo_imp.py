from appointment_confirmation_module.core.models.appointment_notification import AppointmentNotification
from appointment_confirmation_module.core.output_ports.appointment_notification_repo_abc import AppointmentNotificationRepoAbc
from appointment_confirmation_module.shell.db.models import Notification


class AppointmentNotificationRepoImp(AppointmentNotificationRepoAbc):
    def save(self, notification: AppointmentNotification) -> None:
        self.save_appointment_notification(notification)

    def save_appointment_notification(self, appointment_notification: AppointmentNotification):
        notifications_to_save = [Notification(
            title=appointment_notification.doctor_notification.get_title(),
            description=appointment_notification.doctor_notification.get_description(),
            created_at=appointment_notification.doctor_notification.get_created_at(),
        ), Notification(
            title=appointment_notification.patient_notification.get_title(),
            description=appointment_notification.patient_notification.get_description(),
            created_at=appointment_notification.patient_notification.get_created_at(),
        )]

        Notification.objects.bulk_create(notifications_to_save)