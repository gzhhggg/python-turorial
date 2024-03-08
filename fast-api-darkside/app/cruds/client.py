from datetime import datetime

import app.models.client as client_model


async def get_clients(skip: int = 0, limit: int = 10, sort: str = "id", order: str = "asc"):
    sort_order = sort if order == "ASC" else f"-{sort}"
    return await client_model.Client.filter(deleted_at=None).order_by(sort_order).offset(skip).limit(limit).all()

async def get_total_client_count():
    return await client_model.Client.filter(deleted_at=None).count()

async def create_client(client_data):
    client_obj = client_model.Client(name=client_data.name)
    await client_obj.save()
    return client_obj


async def update_client(client_id: int, client_data):
    client = await client_model.Client.get(id=client_id)
    client.name = client_data.name
    await client.save()
    return client


async def delete_client(client_id: int):
    client = await client_model.Client.get(id=client_id)
    client.deleted_at = datetime.now()
    await client.save()
