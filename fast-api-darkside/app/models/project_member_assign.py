from tortoise import fields
from tortoise.models import Model


class ProjectMemberAssign(Model):
    id = fields.BigIntField(pk=True)
    project_slot = fields.ForeignKeyField(
        "models.ProjectSlot", related_name="project_slot"
    )
    member = fields.ForeignKeyField(
        "models.Member", related_name="project_member_assigns"
    )
    start_date = fields.DateField()
    end_date = fields.DateField(null=True)
    cost = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "project_member_assigns"

    def __str__(self):
        return self.name
