import uvicorn
from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from tortoise.contrib.fastapi import register_tortoise
from app.routers import client, project, member
from app.config.db import DB_CONFIG
from app.models.admin import Admin
import aioredis


def create_app():
    app = FastAPI()
    app.mount("/admin", admin_app)

    register_tortoise(
        app,
        config=DB_CONFIG,
        generate_schemas=True,  # スタートアップ時にスキーマを自動生成
        add_exception_handlers=True,
    )

    @app.on_event("startup")
    async def startup():
        # 非同期Redisクライアントのインスタンスを取得
        redis = await aioredis.from_url("redis://localhost", encoding="utf8")
        await admin_app.configure(
            logo_url="https://preview.tabler.io/static/logo-white.svg",
            providers=[
                UsernamePasswordProvider(
                    admin_model=Admin,
                )
            ],
            redis=redis,
        )

    return app


app_ = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app_", reload=True)
# app.include_router(client.router)
# app.include_router(project.router)
# app.include_router(member.router)
