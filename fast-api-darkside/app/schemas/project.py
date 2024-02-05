from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime


class ProjectBase(BaseModel):
    name: str = Field(..., example="プロジェクトA")
    client_id: int = Field(..., description="クライアントID")
    start_date: date = Field(..., description="プロジェクト開始日")
    end_date: Optional[date] = Field(None, description="プロジェクト終了日")

    # end_date が start_date より後であることを確認するバリデータ
    @validator("end_date", allow_reuse=True)
    def validate_dates(cls, end_date, values, **kwargs):
        if end_date and "start_date" in values and end_date <= values["start_date"]:
            raise ValueError("end_date must be after start_date")
        return end_date


class ProjectCreate(ProjectBase):
    pass


class ProjectCreateResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class Project(ProjectBase):
    id: int
    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
