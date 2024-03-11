import json
from typing import List

from fastapi import APIRouter, Query, Response

import app.cruds.client as client_crud
from app.models.client import ClientPydantic, ClientPydanticCreate

router = APIRouter()


@router.get("/clients", response_model=List[ClientPydantic])
async def get_clients(response: Response,
                    sort: str = Query('["id","ASC"]'),
                    range: str = Query('[0,9]'),
                    filter: str = Query("{}")):
    # パラメータを解析
    sort = json.loads(sort)
    range = json.loads(range)
    filter = json.loads(filter)

    # getManyの処理
    if 'ids' in filter:
        ids = filter['ids']
        total, clients = await client_crud.get_many_clients(ids)
        start, end = 0, total - 1
    else:
    # getListの処理
        start, end = range
        total, clients = await client_crud.get_clients_list(start, end-start+1, sort, filter)

    response.headers['Content-Range'] = f'{start}-{end}/{total}'
    return clients

@router.get("/clients/{client_id}", response_model=ClientPydantic)
async def get_client(client_id: int):
    client = await client_crud.get_client(client_id)
    return client

@router.post("/clients", response_model=ClientPydantic)
async def create_client(client: ClientPydanticCreate):
    created_client = await client_crud.create_client(client)
    return created_client

@router.put("/clients/{client_id}", response_model=ClientPydantic)
async def update_client(client: ClientPydantic):
    updated_client = await client_crud.update_client(client)
    return updated_client


@router.delete("/clients/{client_id}", response_model=None, status_code=204)
async def delete_client(client_id: int):
    await client_crud.delete_client(client_id)
    return

@router.delete("/clients", response_model=None, status_code=204)
async def delete_many_client(filter: str = Query("{}")):
    filter_dict = json.loads(filter)
    await client_crud.delete_many_client(filter_dict["id"])
    return {"data": filter_dict["id"]}
