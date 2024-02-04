from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ClientBase(BaseModel):
    name: str = Field(..., example="中村太郎")


class ClientCreate(ClientBase):
    pass


class ClientCreateResponse(ClientCreate):
    id: int

    class Config:
        orm_mode = True


# クライアントを読み込む時に使用されるスキーマ（レスポンスモデル）
class Client(ClientBase):
    id: int
    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
