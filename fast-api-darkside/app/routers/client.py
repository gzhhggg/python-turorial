from fastapi import APIRouter, HTTPException
from typing import List
import app.schemas.client as client_schema
from app.models.client import Client as ClientModel

router = APIRouter()


@router.get("/clients", response_model=List[client_schema.Client])
async def list_clients():
    return [
        client_schema.Client(
            id=1,
            name="田中太郎",
            created_at="2000-01-01 00:00:00",
            deleted_at=None,
        )
    ]


@router.post("/clients", response_model=client_schema.ClientCreateResponse)
async def create_client(client_body: client_schema.ClientCreate):
    return client_schema.ClientCreateResponse(id=1, **client_body.model_dump())


@router.put("/clients/{client_id}")
async def update_client():
    pass


@router.delete("/clients/{client_id}")
async def delete_client():
    pass


# @router.post("/clients/", response_model=Client)
# async def create_client(client: ClientCreate):
#     client_obj = await ClientModel.create(**client.dict())
#     return client_obj


# @router.get("/clients/", response_model=List[Client])
# async def get_clients():
#     clients = await ClientModel.all()
#     return clients


# @router.get("/clients/{client_id}", response_model=Client)
# async def get_client(client_id: int):
#     client = await ClientModel.get_or_none(id=client_id)
#     if client is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return client


# @router.put("/clients/{client_id}", response_model=Client)
# async def update_client(client_id: int, client: ClientCreate):
#     client_update = await ClientModel.get_or_none(id=client_id)
#     if client_update is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     client_update.name = client.name
#     await client_update.save()
#     return client_update


# @router.delete("/clients/{client_id}", response_model=Client)
# async def delete_client(client_id: int):
#     client_del = await ClientModel.get_or_none(id=client_id)
#     if client_del is None:
#         raise HTTPException(status_code=404, detail="Client not found")
#     await client_del.delete()
#     return client_del
