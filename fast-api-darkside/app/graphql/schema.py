
from typing import List

import strawberry
from app.cruds.client import get_clients
from app.models.client import ClientPydantic


@strawberry.experimental.pydantic.type(model=ClientPydantic, all_fields=True)
class ClientType:
    pass

@strawberry.type
class Query:
    @strawberry.field
    async def clients() -> List[ClientType]:
        return await get_clients()

schema = strawberry.Schema(query=Query)
