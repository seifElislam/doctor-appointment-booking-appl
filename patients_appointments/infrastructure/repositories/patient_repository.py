from patients_appointments.domain.exceptions.patient_exceptions import PatientDoesNotExist
from patients_appointments.domain.interfaces.repositories import PatientRepositoryInterface
from patients_appointments.infrastructure.db.models.patient_entity import Patient as PatientModel

class PatientRepository(PatientRepositoryInterface):
    def get_patient_by_id(self, patient_id: int):
        try:
            patient = PatientModel.objects.get(id=patient_id)
            return patient.to_domain()
        except PatientModel.DoesNotExist:
            return PatientDoesNotExist(patient_id)

    def list_patients(self):
        patients = PatientModel.objects.all()
        return [patient.to_domain() for patient in patients]

    def save_patient(self, patient):
        patient_model = PatientModel(
            name=patient.name,
            email=patient.email,
            phone=patient.phone
        )
        if patient.id:
            patient_model.id = patient.id
            
        patient_model.save()
        return patient_model.to_domain()