from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from .config.db import DB_CONFIG
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


# データベース初期化
async def init_db():
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise._drop_databases()
    await Tortoise.generate_schemas()


def create_app():
    app = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        # 作成時にデータベースを初期化する場合はここをアンコメント
        # await init_db()
        await configure_admin(app)  # FastAPI-Adminを設定

    register_tortoise(
        app,
        config=DB_CONFIG,
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
