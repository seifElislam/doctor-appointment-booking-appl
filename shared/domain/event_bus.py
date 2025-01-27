from .event_bus_interface import EventBusInterface


class EventBus(EventBusInterface):
    def __init__(self):
        self.subscribers = {}

    def publish(self, event_name: str, payload: dict) -> None:
        if event_name in self.subscribers:
            for handler in self.subscribers[event_name]:
                handler(payload)

    def subscribe(self, event_name: str, handler: callable) -> None:
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(handler)

