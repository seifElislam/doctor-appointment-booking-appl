from appointment_confirmation_module.core.input_ports.appointment_notification_port import AppointmentNotificationPort
from appointment_confirmation_module.core.models.appointment_notification import AppointmentNotification
from appointment_confirmation_module.core.models.doctor import Doctor
from appointment_confirmation_module.core.models.patient import Patient
from appointment_confirmation_module.core.models.slot import Slot
from appointment_confirmation_module.core.output_ports.appointment_notification_repo_abc import NotificationRepoAbc
from appointment_confirmation_module.core.services.notification_sender_service import NotificationSenderService
from appointment_confirmation_module.shell.db.repos.appointment_notification_repo_imp import NotificationRepoImp
from appointment_confirmation_module.shell.services.notifcation_providers.simple_notification_provider import SimpleNotificationProvider


class AppointmentNotificationAdapter(AppointmentNotificationPort):
    def __init__(self):
        notification_providers = [
            SimpleNotificationProvider()
        ]
        self.send_notification_service = NotificationSenderService(providers=notification_providers)
        self.notification_repo:NotificationRepoAbc = NotificationRepoImp()

    def notify(self, slot:Slot):
        appointment_notification = AppointmentNotification(slot=slot)
        doctor_notification, patient_notification = appointment_notification.get_notifications()
        self.send_notification_service.send(doctor_notification)
        self.send_notification_service.send(patient_notification)
        self.notification_repo.save(doctor_notification)
        self.notification_repo.save(patient_notification)
