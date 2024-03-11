from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.routers import (
    client,
    member,
    member_cost,
    project,
    project_budget,
    project_member_assign,
    project_slot,
)

from .admin.main import configure_admin
from .config.db import TORTOISE_ORM


def create_app(config=TORTOISE_ORM):
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 実運用では具体的なオリジンに限定することが推奨されます
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
    # graphql_app = GraphQLRouter(schema)

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
    # app.include_router(graphql_app, prefix="/graphql")  # GraphQLエンドポイントを追加

    return app

app = create_app()
