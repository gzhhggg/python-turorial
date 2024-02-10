import pytest


@pytest.mark.asyncio
async def test_create_client(app):
    test_client_name = "Test Client"
    response = await app.post("/clients", json={"name": test_client_name})
    assert response.status_code == 200
    assert response.json()["name"] == test_client_name


@pytest.mark.asyncio
async def test_get_clients(app):
    response = await app.get("/clients")
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_update_client(app):
    response = await app.put("/clients/1", json={"name": "Updated Client"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Client"


@pytest.mark.asyncio
async def test_delete_client(app):
    response = await app.delete("/clients/1")
    assert response.status_code == 204
