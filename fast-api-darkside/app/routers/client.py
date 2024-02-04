from fastapi import APIRouter, HTTPException
from typing import List
import app.cruds.client as client_crud
import app.schemas.client as client_schema

router = APIRouter()


@router.post("/clients", response_model=client_schema.ClientCreateResponse)
async def create_client(client: client_schema.ClientCreate):
    created_client = await client_crud.create_client(client)
    return created_client


@router.get("/clients", response_model=List[client_schema.Client])
async def get_clients():
    clients = await client_crud.get_clients()
    return clients


@router.put("/clients/{client_id}", response_model=client_schema.Client)
async def update_client(client_id: int, client: client_schema.ClientCreate):
    updated_client = await client_crud.update_client(client_id, client)
    return updated_client


@router.delete("/clients/{client_id}", response_model=None, status_code=204)
async def delete_client(client_id: int):
    await client_crud.delete_client(client_id)
    return {"message": "Client successfully deleted"}
