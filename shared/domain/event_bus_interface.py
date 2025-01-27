from abc import ABC, abstractmethod


class EventBusInterface(ABC):
    @abstractmethod
    def publish(self, event_name: str, payload: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def subscribe(self, event_name: str, handler: callable) -> None:
        raise NotImplementedError
