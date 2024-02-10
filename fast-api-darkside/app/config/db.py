## TORTOISE_ORMの設定情報
# TODO:本番と開発で管理できるようにする

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

TORTOISE_ORM = {
    "connections": {
        # "default" は Tortoise-ORM 内で使用する接続名です。
        "default": "mysql://docker:docker@localhost:33071/database"
    },
    "apps": {
        "models": {
            # モデルを定義している Python モジュールへのパス
            "models": [
                # TODO: models/__init__.pyで読み込むように設定する？
                "app.models",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
    "use_tz": True,  # タイムゾーンを設定する場合はTrue
    "timezone": "Asia/Tokyo",
}
