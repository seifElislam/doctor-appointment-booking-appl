from dependency_injector import containers, providers
from patients_appointments.infrastructure.gateways.gateway import Gateway
from patients_appointments.infrastructure.repositories.appointment_repository import AppointmentRepository
from patients_appointments.infrastructure.repositories.patient_repository import PatientRepository
from patients_appointments.infrastructure.repositories.slot_repository import SlotRepository
from patients_appointments.infrastructure.repositories.doctor_repository import DoctorRepository
from patients_appointments.use_cases.book_appointment import BookAppointmentUseCase
from patients_appointments.use_cases.list_available_appointments import ListAvailableSlotsUseCase


class Container(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(
    #      packages=[
    #          "patients_appointments.infrastructure",
    #         "patients_appointments.use_cases",
    #         "patients_appointments.presentation"
    #     ]
    # )
    appointmet_repository = providers.Factory(
        AppointmentRepository
    )
    
    slot_repository = providers.Factory(
        SlotRepository
    )
    
    patient_repository = providers.Factory(
        PatientRepository
    )
    
    doctor_repository = providers.Factory(
        DoctorRepository
    )
    
    gateway = providers.Factory(
        Gateway
    )
    
    book_appointment_use_case = providers.Factory(
        BookAppointmentUseCase,
        appointment_repository=appointmet_repository,
        slot_repository=slot_repository,
        patient_repository=patient_repository,
        doctor_repository=doctor_repository,
        gateway=gateway
    )
    
    list_available_appointments_use_case = providers.Factory(
        ListAvailableSlotsUseCase,
        repository=slot_repository
    )
    
    gateway= providers.Singleton(
        Gateway
    )