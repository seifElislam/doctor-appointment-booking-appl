"""
Data Transfer module to transfer domain models from/to database
"""
from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Doctor:
    id: int
    name: str
    specialization: str


@dataclass
class Slot:
    id: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    doctor_id: str
    is_reserved: bool
    cost: float
