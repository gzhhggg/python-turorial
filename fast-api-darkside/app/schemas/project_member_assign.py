from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime


class ProjectMemberAssignBase(BaseModel):
    project_id: int = Field(..., description="プロジェクトID")
    member_id: int = Field(..., description="メンバーID")
    cost: int = Field(..., description="コスト")
    start_date: date = Field(..., description="開始日")
    end_date: Optional[date] = Field(None, description="終了日")


class ProjectMemberAssignCreate(ProjectMemberAssignBase):
    @validator("end_date", allow_reuse=True)
    def validate_dates(cls, end_date, values, **kwargs):
        if end_date and "start_date" in values and end_date <= values["start_date"]:
            raise ValueError("終了日は開始日より後でなければなりません")
        return end_date

    pass


class ProjectMemberAssignCreateResponse(ProjectMemberAssignBase):
    id: int

    class Config:
        orm_mode = True


class ProjectMemberAssign(ProjectMemberAssignBase):
    id: int
    created_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
