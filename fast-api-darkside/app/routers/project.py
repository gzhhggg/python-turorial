from fastapi import APIRouter
from typing import List
import app.cruds.project as project_crud
import app.schemas.project as project_schema

router = APIRouter()


@router.post("/projects", response_model=project_schema.ProjectCreateResponse)
async def create_project(project: project_schema.ProjectCreate):
    created_project = await project_crud.create_project(project)
    return created_project


@router.get("/projects", response_model=List[project_schema.Project])
async def get_projects():
    projects = await project_crud.get_projects()
    return projects


@router.put("/projects/{projects_id}", response_model=project_schema.Project)
async def update_projects(projects_id: int, projects: project_schema.ProjectCreate):
    updated_projects = await project_crud.update_project(projects_id, projects)
    return updated_projects


@router.delete("/projects/{projects_id}", response_model=None, status_code=204)
async def delete_projects(projects_id: int):
    await project_crud.delete_project(projects_id)
    return {"message": "projects successfully deleted"}
