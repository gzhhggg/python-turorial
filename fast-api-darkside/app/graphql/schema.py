
from typing import List

import strawberry
from app.models.client import Client, ClientPydantic


async def get_clients():
    clients_query = await Client.filter(deleted_at=None).all()
    # ClientインスタンスをClientPydanticインスタンスに変換
    clients_pydanitc = [ClientPydantic.from_orm(client) for client in clients_query]
    return clients_pydanitc

@strawberry.experimental.pydantic.type(model=ClientPydantic, all_fields=True)
class ClientType:
    pass

@strawberry.type
class Query:
    @strawberry.field
    async def clients() -> List[ClientType]:
        client_list = await get_clients()
        return client_list

schema = strawberry.Schema(query=Query)
