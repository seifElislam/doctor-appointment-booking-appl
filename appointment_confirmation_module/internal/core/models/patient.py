from dataclasses import dataclass


@dataclass
class Patient:
    id : int
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
