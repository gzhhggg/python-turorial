from fastapi import APIRouter
from typing import List
import app.cruds.member as member_crud
import app.schemas.member as member_schema

router = APIRouter()


@router.post("/members", response_model=member_schema.MemberCreateResponse)
async def create_member(member: member_schema.MemberCreate):
    created_member = await member_crud.create_member(member)
    return created_member


@router.get("/members", response_model=List[member_schema.Member])
async def get_members():
    members = await member_crud.get_members()
    return members


@router.put("/members/{members_id}", response_model=member_schema.Member)
async def update_members(members_id: int, members: member_schema.MemberCreate):
    updated_members = await member_crud.update_member(members_id, members)
    return updated_members


@router.delete("/members/{members_id}", response_model=None, status_code=204)
async def delete_members(members_id: int):
    await member_crud.delete_member(members_id)
    return {"message": "members successfully deleted"}
