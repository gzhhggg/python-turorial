import datetime

from fastapi_admin.models import AbstractAdmin
from tortoise import fields


class Admin(AbstractAdmin):
    last_login = fields.DatetimeField(
        description="Last Login", default=datetime.datetime.now
    )
    email = fields.CharField(max_length=200, default="")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "admins"

    def __str__(self):
        return self.name
