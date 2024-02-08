from tortoise import fields
from tortoise.models import Model


class ProjectSlot(Model):
    id = fields.BigIntField(pk=True)
    project = fields.ForeignKeyField("models.Project", related_name="project_slots")
    name = fields.CharField(max_length=255)
    start_date = fields.DateField()
    end_date = fields.DateField(null=True)
    budget = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table_name = "project_slots"

    def __str__(self):
        return self.name
