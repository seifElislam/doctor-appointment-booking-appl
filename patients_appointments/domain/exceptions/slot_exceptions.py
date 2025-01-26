class SlotIsReservedException(Exception):
    
    def __init__(self):
        super().__init__("Slot is already reserved")

class SlotDoesNotExistException(Exception):
    
    def __init__(self, slot_id: int):
        self.message = f"Slot with id {slot_id} not found."
        super().__init__(self.message)