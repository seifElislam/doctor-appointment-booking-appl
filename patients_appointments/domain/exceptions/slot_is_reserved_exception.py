class SlotIsReservedException(Exception):
    
    def __init__(self):
        super().__init__("Slot is already reserved")
        