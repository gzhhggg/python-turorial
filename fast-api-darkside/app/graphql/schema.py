from typing import List, Optional

import strawberry
from app.cruds.client import create_client, delete_client, get_clients, update_client
from app.schemas.client import ClientCreate


@strawberry.type
class Client:
    id: int
    name: str
    created_at: Optional[str]
    deleted_at: Optional[str]

@strawberry.type
class Query:
    @strawberry.field
    async def clients(self) -> List[Client]:
        clients = await get_clients()
        return [
            Client(
                id=client.id,
                name=client.name,
                created_at=str(client.created_at) if client.created_at else None,
                deleted_at=str(client.deleted_at) if client.deleted_at else None
            ) for client in clients
        ]

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_client(self, name: str) -> Client:
        client = await create_client(ClientCreate(name=name))
        return Client(**client.__dict__)

    @strawberry.mutation
    async def update_client(self, id: int, name: str) -> Client:
        client = await update_client(id, ClientCreate(name=name))
        return Client(**client.__dict__)

    @strawberry.mutation
    async def delete_client(self, id: int) -> str:
        await delete_client(id)
        return "Client successfully deleted"

schema = strawberry.Schema(query=Query, mutation=Mutation)
