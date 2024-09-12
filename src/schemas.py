from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PatientBase(BaseModel):
    patient_id: Optional[int] = None
    fisrt_name: str
    last_name: str
    email: str
    address: str
    city: str
    postal_code: str
    state: str
    date_of_birth: datetime
    state: str
    created_at: datetime
    updated_at: datetime


class PatientCreate(PatientBase):
    pass
