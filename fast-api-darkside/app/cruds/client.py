import app.models.client as client_model
import app.schemas.client as client_schema


async def create_client(client_data: client_schema.ClientCreate):
    client_obj = client_model.Client(name=client_data.name)
    await client_obj.save()
    return client_obj
