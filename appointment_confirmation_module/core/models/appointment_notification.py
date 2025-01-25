from dataclasses import dataclass

from appointment_confirmation_module.core.models.notification import Notification
from appointment_confirmation_module.core.models.slot import Slot


@dataclass
class AppointmentNotification:
    slot: Slot

    doctor_notification: Notification
    patient_notification: Notification

    def __init__(self, slot: Slot):
        self.slot = slot
        self.make_slot_notification()

    def make_doctor_notification(self):
        self.doctor_notification = Notification.create_notification(
            title="Appointment scheduled with patient",
            description=f"Your appointment with patient {self.slot.get_patient().get_name()} is scheduled at {self.slot.get_date()}",
           receiver_id= self.slot.get_doctor().get_id()
        )

    def make_patient_notification(self):
        self.patient_notification = Notification.create_notification(
            title="Appointment scheduled with doctor",
            description=f"Your appointment with doctor {self.slot.get_doctor().get_name()} is scheduled at {self.slot.get_date()}",
            receiver_id= self.slot.get_patient().get_id()
        )

    def make_slot_notification(self):
        self.make_doctor_notification()
        self.make_patient_notification()

    def get_notifications(self):
        return self.doctor_notification, self.patient_notification
