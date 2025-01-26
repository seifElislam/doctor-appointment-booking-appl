from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    name: str

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
