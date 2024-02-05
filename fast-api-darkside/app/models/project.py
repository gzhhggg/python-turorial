from tortoise import fields
from tortoise.models import Model


class Project(Model):
    id = fields.BigIntField(pk=True)
    client = fields.ForeignKeyField("models.Client", related_name="projects")
    name = fields.CharField(max_length=255)
    start_date = fields.DateField()
    end_date = fields.DateField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "projects"
