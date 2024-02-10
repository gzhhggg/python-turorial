from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from .config.db import TORTOISE_ORM
from .admin.main import configure_admin
from app.routers import (
    client,
    project,
    member,
    project_slot,
    project_budget,
    project_member_assign,
    member_cost,
)


def create_app(config=TORTOISE_ORM):
    app = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        await configure_admin(app)  # FastAPI-Adminを設定

    register_tortoise(
        app,
        config=config,
        generate_schemas=True,  # スタートアップ時にスキーマを自動生成
        add_exception_handlers=True,
    )

    app.include_router(client.router)
    app.include_router(project.router)
    app.include_router(member.router)
    app.include_router(project_slot.router)
    app.include_router(project_budget.router)
    app.include_router(project_member_assign.router)
    app.include_router(member_cost.router)

    return app


app = create_app()
