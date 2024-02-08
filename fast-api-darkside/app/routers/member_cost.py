from fastapi import APIRouter
from typing import List
import app.cruds.member_cost as member_cost_crud
import app.schemas.member_cost as member_cost_schema

router = APIRouter()


@router.post(
    "/member_cost",
    response_model=member_cost_schema.MemberCostCreateResponse,
)
async def create_member_cost(
    member_cost: member_cost_schema.MemberCostCreate,
):
    created_member_cost = await member_cost_crud.create_member_cost(member_cost)
    return created_member_cost


@router.get(
    "/member_cost",
    response_model=List[member_cost_schema.MemberCost],
)
async def get_member_cost():
    member_cost = await member_cost_crud.get_member_costs()
    return member_cost


@router.put(
    "/member_cost/{member_cost_id}",
    response_model=member_cost_schema.MemberCost,
)
async def update_member_cost(
    member_cost_id: int,
    member_cost: member_cost_schema.MemberCostCreate,
):
    updated_member_cost = await member_cost_crud.update_member_cost(
        member_cost_id, member_cost
    )
    return updated_member_cost


@router.delete(
    "/member_cost/{member_cost_id}",
    response_model=None,
    status_code=204,
)
async def delete_member_cost(member_cost_id: int):
    await member_cost_crud.delete_member_cost(member_cost_id)
    return {"message": "Project member_assign successfully deleted"}
