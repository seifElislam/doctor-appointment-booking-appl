from patients_appointments.domain.interfaces.repositories import SlotRepositoryInterface

from patients_appointments.infrastructure.db.models.slot_entity import Slot

class SlotRepository(SlotRepositoryInterface):
    
    def get_slot_by_id(self, slot_id):
        try:
            slot = Slot.objects.get(id=slot_id)
            return slot.to_domain()
        except Slot.DoesNotExist:
            raise Slot.DoesNotExist(f"Slot with id {slot_id} does not exist")
    
    def list_slots(self, doctor_id):
        return [slot.to_domain() for slot in Slot.objects.filter(doctor_id=doctor_id)]
    
    def list_available_slots(self, doctor_id):
        return [slot.to_domain() for slot in Slot.objects.filter(doctor_id=doctor_id, is_reserved=False)]   
        