from datetime import datetime
import app.models.project as project_model
import app.schemas.project as project_schema


async def create_project(project_data: project_schema.ProjectCreate):
    project_obj = project_model.Project(
        name=project_data.name,
        client_id=project_data.client_id,  # ForeignKey として client_id を設定
        start_date=project_data.start_date,
        end_date=project_data.end_date,  # end_date は Optional なので、None の場合がある
    )
    await project_obj.save()
    return project_obj


async def get_projects():
    return await project_model.Project.filter(deleted_at=None)


async def update_project(project_id: int, project_data: project_schema.ProjectCreate):
    project_obj = await project_model.Project.get(id=project_id)
    project_obj.name = project_data.name
    project_obj.start_date = project_data.start_date
    project_obj.end_date = project_data.end_date
    await project_obj.save()
    return project_obj


async def delete_project(project_id: int):
    project = await project_model.Project.get(id=project_id)
    project.deleted_at = datetime.now()
    await project.save()
