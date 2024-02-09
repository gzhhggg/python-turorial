import os

# Pythonのテストフレームワーク
import pytest

# pytestで非同期関数をテストするためのプラグイン
import pytest_asyncio

# 非同期HTTPクライアント。非同期にHTTPリクエストができる
from httpx import AsyncClient

from app.main import create_app
from tortoise import Tortoise


# 各テスト関数が実行されるたびに、このフィクスチャ関数が非同期で実行されることを指定
@pytest_asyncio.fixture(scope="function")
async def app_client():
    # 環境変数からデータベースURLを取得
    db_url = os.environ.get("DATABASE_URL")
    # Tortoise ORMの初期化とスキーマの生成と初期化
    await Tortoise.init(db_url=db_url, modules={"models": ["app.models"]})
    # データベーススキーマを非同期で生成
    await Tortoise.generate_schemas()

    app = create_app()
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        # AsyncClient インスタンスをそのままテスト関数に渡します。
        yield client

    # テスト終了後のクリーンアップ
    await Tortoise.close_connections()


@pytest.mark.asyncio
async def test_create_client(app_client):
    test_client_name = "Test Client"
    response = await app_client.post("/clients", json={"name": test_client_name})
    assert response.status_code == 200
    assert response.json()["name"] == test_client_name


@pytest.mark.asyncio
async def test_get_clients(app_client):
    response = await app_client.get("/clients")
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_update_client(app_client):
    response = await app_client.put("/clients/1", json={"name": "Updated Client"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Client"


@pytest.mark.asyncio
async def test_delete_client(app_client):
    response = await app_client.delete("/clients/1")
    assert response.status_code == 204
