import json
from typing import List

from fastapi import APIRouter, Query, Response

import app.cruds.member as member_crud
from app.models.member import MemberPydantic, MemberPydanticCreate
from app.schemas.member import Member

router = APIRouter()


@router.get("/members", response_model=List[Member])
async def get_members(response: Response,
                    sort: str = Query('["id","ASC"]'),
                    range: str = Query('[0,9]'),
                    filter: str = Query("{}")):
    # パラメータを解析
    sort = json.loads(sort)
    range = json.loads(range)
    filter = json.loads(filter)

    # getManyの処理
    if 'ids' in filter:
        ids = filter['ids']
        total, members = await member_crud.get_many_members(ids)
        start, end = 0, total - 1
    else:
    # getListの処理
        start, end = range
        total, members = await member_crud.get_members_list(start, end-start+1, sort, filter)

    response.headers['Content-Range'] = f'{start}-{end}/{total}'
    return members

@router.get("/members/{member_id}", response_model=MemberPydantic)
async def get_member(member_id: int):
    member = await member_crud.get_member(member_id)
    return member

@router.post("/members", response_model=MemberPydantic)
async def create_member(member: MemberPydanticCreate):
    created_member = await member_crud.create_member(member)
    return created_member

@router.put("/members/{member_id}", response_model=MemberPydantic)
async def update_member(member: MemberPydantic):
    updated_member = await member_crud.update_member(member)
    return updated_member


@router.delete("/members/{member_id}", response_model=None, status_code=204)
async def delete_member(member_id: int):
    await member_crud.delete_member(member_id)
    return

@router.delete("/members", response_model=None, status_code=204)
async def delete_many_member(filter: str = Query("{}")):
    filter_dict = json.loads(filter)
    await member_crud.delete_many_member(filter_dict["id"])
    return {"data": filter_dict["id"]}
