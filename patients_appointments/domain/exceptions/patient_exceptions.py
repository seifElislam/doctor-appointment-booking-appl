class PatientDoesNotExist(Exception):
    def __init__(self, patient_id: int):
        self.message = f"Patient with id {patient_id} does not exist"
        super().__init__(self.message)