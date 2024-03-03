import strawberry
from tortoise import fields
from tortoise.models import Model


class Client(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "clients"

    def __str__(self):
        return self.name

@strawberry.experimental.pydantic.type(model=Client, all_fields=True)
class ClientType:
    pass