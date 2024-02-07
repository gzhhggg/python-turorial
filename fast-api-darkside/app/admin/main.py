import os
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from ..config.db import DB_CONFIG
from ..models.admin import Admin
from aioredis import from_url as aioredis_from_url
from .constants import BASE_DIR


async def configure_admin(app):
    redis = await aioredis_from_url("redis://127.0.0.1:6379", encoding="utf8")
    await admin_app.configure(
        template_folders=[os.path.join(BASE_DIR, "templates")],
        providers=[
            UsernamePasswordProvider(
                login_logo_url="https://preview.tabler.io/static/logo.svg",
                admin_model=Admin,
            )
        ],
        redis=redis,
    )
    app.mount("/admin", admin_app)
