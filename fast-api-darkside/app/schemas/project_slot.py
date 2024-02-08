from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime


class ProjectSlotBase(BaseModel):
    project_id: int = Field(..., description="プロジェクトID")
    name: str = Field(..., example="エンジニア")
    start_date: date = Field(..., description="募集開始日")
    end_date: Optional[date] = Field(None, description="募集終了日")
    budget: int = Field(..., description="予算")


class ProjectSlotCreate(ProjectSlotBase):
    @validator("end_date", allow_reuse=True)
    def validate_dates(cls, end_date, values, **kwargs):
        if end_date and "start_date" in values and end_date <= values["start_date"]:
            raise ValueError("終了日は開始日より後でなければなりません")
        return end_date

    pass


class ProjectSlotCreateResponse(ProjectSlotBase):
    id: int

    class Config:
        orm_mode = True


class ProjectSlot(ProjectSlotBase):
    id: int
    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
