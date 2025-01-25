from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    name: str
    email: str
    phone: str
    