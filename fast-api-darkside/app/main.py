from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers import client
from .config import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # スタートアップ時にスキーマを自動生成
    add_exception_handlers=True,
)


app.include_router(client.router)
