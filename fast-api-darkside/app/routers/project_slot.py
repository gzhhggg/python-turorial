from fastapi import APIRouter
from typing import List
import app.cruds.project_slot as project_slot_crud
import app.schemas.project_slot as project_slot_schema

router = APIRouter()


@router.post(
    "/project_slots", response_model=project_slot_schema.ProjectSlotCreateResponse
)
async def create_project_slot(project_slot: project_slot_schema.ProjectSlotCreate):
    created_project_slot = await project_slot_crud.create_project_slot(project_slot)
    return created_project_slot


@router.get("/project_slots", response_model=List[project_slot_schema.ProjectSlot])
async def get_project_slots():
    project_slots = await project_slot_crud.get_project_slots()
    return project_slots


@router.put(
    "/project_slots/{project_slot_id}", response_model=project_slot_schema.ProjectSlot
)
async def update_project_slot(
    project_slot_id: int, project_slot: project_slot_schema.ProjectSlotCreate
):
    updated_project_slot = await project_slot_crud.update_project_slot(
        project_slot_id, project_slot
    )
    return updated_project_slot


@router.delete("/project_slots/{project_slot_id}", response_model=None, status_code=204)
async def delete_project_slot(project_slot_id: int):
    await project_slot_crud.delete_project_slot(project_slot_id)
    return {"message": "Project slot successfully deleted"}
