from typing import List
from dependency_injector.wiring import inject, Provide
from patients_appointments.domain.entities.slot import Slot
from patients_appointments.domain.interfaces.repositories import SlotRepositoryInterface

class ListAvailableSlotsUseCase:
    @inject
    def __init__(self, repository: SlotRepositoryInterface = Provide[SlotRepositoryInterface]):
        self.repository = repository

    def execute(self, doctor_id:int) -> List[Slot]:
        return self.repository.list_available_slots(doctor_id=doctor_id)