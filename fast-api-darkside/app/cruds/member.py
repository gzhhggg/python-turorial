from datetime import datetime

import app.models.member as member_model


async def get_members_list(start: int, limit: int, sort: list, filter: dict):
    # ソート条件を解析
    sort_field, sort_order = sort
    sort_query = sort_field if sort_order == "ASC" else f"-{sort_field}"

    # フィルタ条件の構築
    filter_query = {}
    for key, value in filter.items():
        if key == "q":  # 検索クエリの場合、名前でフィルタリング
            filter_query["name__icontains"] = value

    members_query = member_model.Member.filter(**filter_query).order_by(sort_query)
    total = await members_query.count()
    members = await members_query.offset(start).limit(limit).all()

    return total, members

async def get_member(member_id: int):
    member = await member_model.Member.get(id=member_id)
    return member

async def get_many_members(member_ids: list[int]):
    filter_query = {"id__in": member_ids}
    members_query = member_model.Member.filter(**filter_query)
    total = await members_query.count()
    members = await members_query.all()

    return total, members

async def create_member(member_data):
    member_obj = member_model.Member(name=member_data.name)
    await member_obj.save()
    return member_obj


async def update_member(member_data):
    member = await member_model.Member.get(id=member_data.id)
    member.name = member_data.name
    await member.save()
    return member


async def delete_member(member_id: int):
    member = await member_model.Member.get(id=member_id)
    member.deleted_at = datetime.now()
    await member.save()
    return member

async def delete_many_member(member_ids: list[int]):
    await member_model.Member.filter(id__in=member_ids).update(deleted_at=datetime.now())
