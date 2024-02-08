from fastapi import APIRouter
from typing import List
import app.cruds.project_member_assign as project_member_assign_crud
import app.schemas.project_member_assign as project_member_assign_schema

router = APIRouter()


@router.post(
    "/project_member_assign",
    response_model=project_member_assign_schema.ProjectMemberAssignCreateResponse,
)
async def create_project_member_assign(
    project_member_assign: project_member_assign_schema.ProjectMemberAssignCreate,
):
    created_project_member_assign = (
        await project_member_assign_crud.create_project_member_assign(
            project_member_assign
        )
    )
    return created_project_member_assign


@router.get(
    "/project_member_assign",
    response_model=List[project_member_assign_schema.ProjectMemberAssign],
)
async def get_project_member_assign():
    project_member_assign = (
        await project_member_assign_crud.get_project_member_assigns()
    )
    return project_member_assign


@router.put(
    "/project_member_assign/{project_member_assign_id}",
    response_model=project_member_assign_schema.ProjectMemberAssign,
)
async def update_project_member_assign(
    project_member_assign_id: int,
    project_member_assign: project_member_assign_schema.ProjectMemberAssignCreate,
):
    updated_project_member_assign = (
        await project_member_assign_crud.update_project_member_assign(
            project_member_assign_id, project_member_assign
        )
    )
    return updated_project_member_assign


@router.delete(
    "/project_member_assign/{project_member_assign_id}",
    response_model=None,
    status_code=204,
)
async def delete_project_member_assign(project_member_assign_id: int):
    await project_member_assign_crud.delete_project_member_assign(
        project_member_assign_id
    )
    return {"message": "Project member_assign successfully deleted"}
