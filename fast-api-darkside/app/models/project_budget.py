from tortoise import fields
from tortoise.models import Model


class ProjectBudget(Model):
    id = fields.BigIntField(pk=True)
    project = fields.ForeignKeyField("models.Project", related_name="project_budgets")
    start_date = fields.DateField()
    end_date = fields.DateField(null=True)
    budget = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table_name = "project_budgets"

    def __str__(self):
        return self.name
