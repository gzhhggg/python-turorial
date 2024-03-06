from typing import List

from fastapi import APIRouter

import app.cruds.client as client_crud
from app.models.client import ClientPydantic, ClientPydanticCreate

router = APIRouter()


@router.post("/clients", response_model=ClientPydanticCreate)
async def create_client(client: ClientPydanticCreate):
    created_client = await client_crud.create_client(client)
    return created_client


@router.get("/clients", response_model=List[ClientPydantic])
async def get_clients():
    clients = await client_crud.get_clients()
    return clients


@router.put("/clients/{client_id}", response_model=ClientPydantic)
async def update_client(client_id: int, client: ClientPydanticCreate):
    updated_client = await client_crud.update_client(client_id, client)
    return updated_client


@router.delete("/clients/{client_id}", response_model=None, status_code=204)
async def delete_client(client_id: int):
    await client_crud.delete_client(client_id)
    return {"message": "Client successfully deleted"}
