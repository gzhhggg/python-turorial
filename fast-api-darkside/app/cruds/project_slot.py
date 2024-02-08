from datetime import datetime
import app.models.project_slot as project_slot_model
import app.schemas.project_slot as project_slot_schema  # Assuming this exists


async def create_project_slot(project_slot_data: project_slot_schema.ProjectSlotCreate):
    project_slot_obj = project_slot_model.ProjectSlot(
        project_id=project_slot_data.project_id,
        name=project_slot_data.name,
        start_date=project_slot_data.start_date,
        end_date=project_slot_data.end_date,  # Optional, can be None
        budget=project_slot_data.budget,
    )
    await project_slot_obj.save()
    return project_slot_obj


async def get_project_slots():
    return await project_slot_model.ProjectSlot.filter(deleted_at=None)


async def update_project_slot(
    project_slot_id: int, project_slot_data: project_slot_schema.ProjectSlotCreate
):
    project_slot_obj = await project_slot_model.ProjectSlot.get(id=project_slot_id)
    project_slot_obj.name = project_slot_data.name
    project_slot_obj.start_date = project_slot_data.start_date
    project_slot_obj.end_date = project_slot_data.end_date
    project_slot_obj.budget = project_slot_data.budget
    await project_slot_obj.save()
    return project_slot_obj


async def delete_project_slot(project_slot_id: int):
    project_slot = await project_slot_model.ProjectSlot.get(id=project_slot_id)
    project_slot.deleted_at = datetime.now()
    await project_slot.save()
