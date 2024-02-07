from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .config.db import DB_CONFIG
from .admin.main import configure_admin
# from app.routers import client, project, member


def create_app():
    app = FastAPI()

    register_tortoise(
        app,
        config=DB_CONFIG,
        generate_schemas=True,  # スタートアップ時にスキーマを自動生成
        add_exception_handlers=True,
    )

    @app.on_event("startup")
    async def startup_event():
        await configure_admin(app)  # FastAPI-Adminを設定

    return app


app = create_app()

# app.include_router(client.router)
# app.include_router(project.router)
# app.include_router(member.router)doi
