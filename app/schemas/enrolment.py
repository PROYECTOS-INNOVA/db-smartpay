from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class EnrolmentBase(BaseModel):
    user_id: UUID
    vendor_id: UUID


class EnrolmentCreate(EnrolmentBase):
    pass


class EnrolmentUpdate(BaseModel):
    # Ajusta los campos según EnrolmentBase, todos opcionales y None por defecto
    pass


class EnrolmentDB(EnrolmentBase):
    enrolment_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
