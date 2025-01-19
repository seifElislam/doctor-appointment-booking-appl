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
    
    def save_slot(self, slot):
        if slot.id is None:
            django_slot = Slot(
                time=slot.time,
                doctor_id=slot.doctor_id,
                doctor_name=slot.doctor_name,
                is_reserved=slot.is_reserved
            )
            print("[[[[[[[[[[[[[[[[django_slot]]]]]]]]]]]]]]]]")
            print(django_slot)
        else:
            django_slot = Slot.objects.get(id=slot.id)
            django_slot.time = slot.time
            django_slot.doctor_id = slot.doctor_id
            django_slot.doctor_name = slot.doctor_name
            django_slot.is_reserved = slot.is_reserved
            
        django_slot.save()