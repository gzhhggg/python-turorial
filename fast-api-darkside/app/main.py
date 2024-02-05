from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers import client, project, member
from app.config.db import DB_CONFIG

app = FastAPI()

register_tortoise(
    app,
    config=DB_CONFIG,
    generate_schemas=True,  # スタートアップ時にスキーマを自動生成
    add_exception_handlers=True,
)


app.include_router(client.router)
app.include_router(project.router)
app.include_router(member.router)
