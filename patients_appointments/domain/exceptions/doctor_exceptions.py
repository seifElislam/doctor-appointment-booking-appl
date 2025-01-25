class DoctorDoesNotExistException(Exception):
    def __init__(self, doctor_id: int):
        self.message = f"Doctor with id {doctor_id} not found."
        super().__init__(self.message)