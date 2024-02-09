from fastapi import APIRouter
from typing import List
import app.cruds.project_budget as project_budget_crud
import app.schemas.project_budget as project_budget_schema

router = APIRouter()


@router.post(
    "/project_budgets", response_model=project_budget_schema.ProjectBudgetCreateResponse
)
async def create_project_budget(
    project_budget: project_budget_schema.ProjectBudgetCreate,
):
    created_project_budget = await project_budget_crud.create_project_budget(
        project_budget
    )
    return created_project_budget


@router.get(
    "/project_budgets", response_model=List[project_budget_schema.ProjectBudget]
)
async def get_project_budgets():
    project_budgets = await project_budget_crud.get_project_budgets()
    return project_budgets


@router.put(
    "/project_budgets/{project_budget_id}",
    response_model=project_budget_schema.ProjectBudget,
)
async def update_project_budget(
    project_budget_id: int, project_budget: project_budget_schema.ProjectBudgetCreate
):
    updated_project_budget = await project_budget_crud.update_project_budget(
        project_budget_id, project_budget
    )
    return updated_project_budget


@router.delete(
    "/project_budgets/{project_budget_id}", response_model=None, status_code=204
)
async def delete_project_budget(project_budget_id: int):
    await project_budget_crud.delete_project_budget(project_budget_id)
    return {"message": "Project budget successfully deleted"}
