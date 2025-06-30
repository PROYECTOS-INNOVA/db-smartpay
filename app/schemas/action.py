from enum import Enum
from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

from app.schemas.user import UserDB


class ActionState(str, Enum):
    APPLIED = "applied"
    PENDING = "pending"
    FAILED = "failed"


class ActionType(str, Enum):
    BLOCK = "block"
    LOCATE = "locate"
    REFRESH = "refresh"
    NOTIFY = "notify"
    UN_ENROLL = "unenroll"
    UN_BLOCK = "unblock"
    EXCEPTION = "exception"


class ActionBase(BaseModel):
    device_id: UUID
    state: ActionState = ActionState.PENDING
    applied_by_id: UUID
    action: ActionType
    description: Optional[str] = None


class ActionCreate(ActionBase):
    pass


class ActionUpdate(BaseModel):
    state: Optional[ActionState] = None
    description: Optional[str] = None


class ActionInDB(ActionBase):
    action_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ActionResponse(BaseModel):
    action_id: UUID
    device_id: UUID
    state: ActionState
    action: ActionType
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    applied_by: UserDB

    class Config:
        orm_mode = True
