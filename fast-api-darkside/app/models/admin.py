import datetime

from fastapi_admin.models import AbstractAdmin
from tortoise import fields


class Admin(AbstractAdmin):
    last_login = fields.DatetimeField(
        description="Last Login", default=datetime.datetime.now
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"