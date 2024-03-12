from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class MemberBase(BaseModel):
    name: str = Field(..., example="山田太郎")
    client_id: int = Field(..., description="クライアントID")
    email: EmailStr = Field(..., example="yamada@example.com")
    phone: str = Field(..., example="090-1234-5678")


class MemberCreate(MemberBase):
    pass


class MemberCreateResponse(MemberBase):
    id: int

    class Config:
        orm_mode = True


class Member(MemberBase):
    id: int
    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
