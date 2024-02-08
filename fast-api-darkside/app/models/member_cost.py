from tortoise import fields
from tortoise.models import Model


class MemberCost(Model):
    id = fields.BigIntField(pk=True)
    member = fields.ForeignKeyField("models.Member", related_name="member_costs")
    start_date = fields.DateField()
    end_date = fields.DateField(null=True)
    cost = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "member_costs"

    def __str__(self):
        return self.name
