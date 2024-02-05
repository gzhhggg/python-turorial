import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from tortoise.contrib.fastapi import register_tortoise
from app.routers import client, project, member
from app.config.db import DB_CONFIG
from app.models import admin
import redis.asyncio as redis


async def get_redis_connection():
    # Redisの非同期接続を作成するためのユーティリティ関数を定義する
    return await redis.Redis(
        host="redis", port=6379, db=0, decode_responses=True, encoding="utf-8"
    )


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
        redis_connection = await get_redis_connection()
        await admin_app.configure(
            logo_url="https://preview.tabler.io/static/logo-white.svg",
            providers=[
                UsernamePasswordProvider(
                    admin_model=admin.Admin,
                )
            ],
            redis=redis_connection,
        )

    return app


app_ = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app_", reload=True)
# app.include_router(client.router)
# app.include_router(project.router)
# app.include_router(member.router)
