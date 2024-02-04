from fastapi import APIRouter, HTTPException
import app.cruds.client as client_crud
import app.schemas.client as client_schema

router = APIRouter()


@router.post("/clients", response_model=client_schema.ClientCreateResponse)
async def create_client(client: client_schema.ClientCreate):
    created_client = await client_crud.create_client(client)
    return created_client
