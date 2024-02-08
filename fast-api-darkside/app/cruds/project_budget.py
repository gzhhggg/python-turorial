from datetime import datetime
import app.models.project_budget as project_budget_model
import app.schemas.project_budget as project_budget_schema  # Assuming this exists


async def create_project_budget(
    project_budget_data: project_budget_schema.ProjectBudgetCreate,
):
    project_budget_obj = project_budget_model.ProjectBudget(
        project_id=project_budget_data.project_id,
        start_date=project_budget_data.start_date,
        end_date=project_budget_data.end_date,  # Optional, can be None
        budget=project_budget_data.budget,
    )
    await project_budget_obj.save()
    return project_budget_obj


async def get_project_budgets():
    return await project_budget_model.ProjectBudget.filter(deleted_at=None)


async def update_project_budget(
    project_budget_id: int,
    project_budget_data: project_budget_schema.ProjectBudgetCreate,
):
    project_budget_obj = await project_budget_model.ProjectBudget.get(
        id=project_budget_id
    )
    project_budget_obj.start_date = project_budget_data.start_date
    project_budget_obj.end_date = project_budget_data.end_date
    project_budget_obj.budget = project_budget_data.budget
    await project_budget_obj.save()
    return project_budget_obj


async def delete_project_budget(project_budget_id: int):
    project_budget = await project_budget_model.ProjectBudget.get(id=project_budget_id)
    project_budget.deleted_at = datetime.now()
    await project_budget.save()
