from dataclasses import dataclass

from appointment_confirmation_module.core.models.patient import Patient

@dataclass
class PatientDTO:
    id: int
    name: str
    email: str
    phone: str

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_phone(self) -> str:
        return self.phone

    def get_id(self):
        return self.id

    def get_patient_domain_model(self):
        return Patient(self.id, self.name, self.email, self.phone)