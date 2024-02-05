from datetime import datetime
import app.models.member as member_model
import app.schemas.member as member_schema


async def create_member(member_data: member_schema.MemberCreate):
    member_obj = member_model.Member(
        name=member_data.name,
        client_id=member_data.client_id,  # ForeignKey として client_id を設定
        email=member_data.email,
        phone=member_data.phone,
    )
    await member_obj.save()
    return member_obj


async def get_members():
    return await member_model.Member.filter(deleted_at=None)


async def update_member(member_id: int, member_data: member_schema.MemberCreate):
    member_obj = await member_model.Member.get(id=member_id)
    member_obj.name = member_data.name
    member_obj.email = member_data.email
    member_obj.phone = member_data.phone
    await member_obj.save()
    return member_obj


async def delete_member(member_id: int):
    member = await member_model.Member.get(id=member_id)
    member.deleted_at = datetime.now()
    await member.save()
