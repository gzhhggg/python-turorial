from datetime import datetime

import app.models.client as client_model


async def get_clients_list(start: int, limit: int, sort: list, filter: dict):
    # ソート条件を解析
    sort_field, sort_order = sort
    sort_query = sort_field if sort_order == "ASC" else f"-{sort_field}"

    # フィルタ条件の構築
    filter_query = {}
    for key, value in filter.items():
        if key == "q":  # 検索クエリの場合、名前でフィルタリング
            filter_query["name__icontains"] = value

    clients_query = client_model.Client.filter(**filter_query).order_by(sort_query)
    total = await clients_query.count()
    clients = await clients_query.offset(start).limit(limit).all()

    return total, clients

async def get_client(client_id: int):
    client = await client_model.Client.get(id=client_id)
    return client

async def get_many_clients(client_ids: list[int]):
    filter_query = {"id__in": client_ids}
    clients_query = client_model.Client.filter(**filter_query)
    total = await clients_query.count()
    clients = await clients_query.all()

    return total, clients

async def create_client(client_data):
    client_obj = client_model.Client(name=client_data.name)
    await client_obj.save()
    return client_obj


async def update_client(client_data):
    client = await client_model.Client.get(id=client_data.id)
    client.name = client_data.name
    await client.save()
    return client


async def delete_client(client_id: int):
    client = await client_model.Client.get(id=client_id)
    client.deleted_at = datetime.now()
    await client.save()
    return client

async def delete_many_client(client_ids: list[int]):
    await client_model.Client.filter(id__in=client_ids).update(deleted_at=datetime.now())
