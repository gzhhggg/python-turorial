from tortoise import fields
from tortoise.models import Model


class Member(Model):
    id = fields.BigIntField(pk=True)
    client = fields.ForeignKeyField("models.Client", related_name="members")
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "members"
