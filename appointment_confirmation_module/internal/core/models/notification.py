from dataclasses import dataclass
from datetime import datetime


@dataclass
class Notification:
    title: str
    description: str
    created_at: datetime
    user_id: int
    def __str__(self) -> str:
        return f"title: {self.title}, description: {self.description}, created_at: {self.created_at}, user_id: {self.user_id}"
    @classmethod
    def create_notification(cls, title: str, description: str , receiver_id) -> 'Notification':
        return Notification(title, description, datetime.now(), receiver_id)

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_user_id(self) -> int:
        return self.user_id

