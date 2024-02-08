from datetime import datetime
import app.models.member_cost as member_cost_model
import app.schemas.member_cost as member_cost_schema  # Assuming this exists


async def create_member_cost(
    member_cost_data: member_cost_schema.MemberCostCreate,
):
    member_cost_obj = member_cost_model.MemberCost(
        project_id=member_cost_data.project_id,
        start_date=member_cost_data.start_date,
        end_date=member_cost_data.end_date,  # Optional, can be None
        cost=member_cost_data.cost,
    )
    await member_cost_obj.save()
    return member_cost_obj


async def get_member_costs():
    return await member_cost_model.MemberCost.filter(deleted_at=None)


async def update_member_cost(
    member_cost_id: int,
    member_cost_data: member_cost_schema.MemberCostCreate,
):
    member_cost_obj = await member_cost_model.MemberCost.get(id=member_cost_id)
    member_cost_obj.cost = member_cost_data.cost
    member_cost_obj.start_date = member_cost_data.start_date
    member_cost_obj.end_date = member_cost_data.end_date
    await member_cost_obj.save()
    return member_cost_obj


async def delete_member_cost(member_cost_id: int):
    member_cost = await member_cost_model.MemberCost.get(id=member_cost_id)
    member_cost.deleted_at = datetime.now()
    await member_cost.save()
