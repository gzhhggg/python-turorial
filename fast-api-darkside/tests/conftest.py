import os
import pytest
import pytest_asyncio
from httpx import AsyncClient
from app.main import create_app
from tortoise import Tortoise


# テスト用のフィクスチャ（テストを実行する際に必要な前提条件や環境を設定する）
@pytest_asyncio.fixture(scope="function")
async def app():
    db_url = os.environ.get("DATABASE_URL")
    await Tortoise.init(db_url=db_url, modules={"models": ["app.models"]})
    await Tortoise.generate_schemas()

    app = create_app()
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

    await Tortoise.close_connections()
