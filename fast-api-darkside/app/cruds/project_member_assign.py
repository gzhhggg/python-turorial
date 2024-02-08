from datetime import datetime
import app.models.project_member_assign as project_member_assign_model
import app.schemas.project_member_assign as project_member_assign_schema  # Assuming this exists


async def create_project_member_assign(
    project_member_assign_data: project_member_assign_schema.ProjectMemberAssignCreate,
):
    project_member_assign_obj = project_member_assign_model.ProjectMemberAssign(
        project_id=project_member_assign_data.project_id,
        start_date=project_member_assign_data.start_date,
        end_date=project_member_assign_data.end_date,  # Optional, can be None
        cost=project_member_assign_data.cost,
    )
    await project_member_assign_obj.save()
    return project_member_assign_obj


async def get_project_member_assigns():
    return await project_member_assign_model.ProjectMemberAssign.filter(deleted_at=None)


async def update_project_member_assign(
    project_member_assign_id: int,
    project_member_assign_data: project_member_assign_schema.ProjectMemberAssignCreate,
):
    project_member_assign_obj = (
        await project_member_assign_model.ProjectMemberAssign.get(
            id=project_member_assign_id
        )
    )
    project_member_assign_obj.cost = project_member_assign_data.cost
    project_member_assign_obj.start_date = project_member_assign_data.start_date
    project_member_assign_obj.end_date = project_member_assign_data.end_date
    await project_member_assign_obj.save()
    return project_member_assign_obj


async def delete_project_member_assign(project_member_assign_id: int):
    project_member_assign = await project_member_assign_model.ProjectMemberAssign.get(
        id=project_member_assign_id
    )
    project_member_assign.deleted_at = datetime.now()
    await project_member_assign.save()
