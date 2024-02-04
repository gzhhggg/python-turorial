from datetime import datetime
import app.models.client as client_model
import app.schemas.client as client_schema


async def create_client(client_data: client_schema.ClientCreate):
    client_obj = client_model.Client(name=client_data.name)
    await client_obj.save()
    return client_obj


async def get_clients():
    return await client_model.Client.filter(deleted_at=None)


async def update_client(client_id: int, client_data: client_schema.ClientCreate):
    client = await client_model.Client.get(id=client_id)
    client.name = client_data.name
    await client.save()
    return client


async def delete_client(client_id: int):
    client = await client_model.Client.get(id=client_id)
    client.deleted_at = datetime.now()
    await client.save()
