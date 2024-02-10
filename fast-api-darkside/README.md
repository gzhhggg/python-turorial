# fast_api を使った darkside アプリ作成

後で整理する！！

## python 関係ない個人メモ(後で消す)

md プレビューショートカット
`cmd + k → v`

## ディレクトリ構想（どうするか検討中）

とりあえず下記で実装してみる
参考：https://zenn.dev/dencyu/articles/a94928b9ce45f7
参考公式：https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#file-structure

```
fast-api-darkside/
│
├── app/
│ ├── **init**.py
│ ├── main.py # FastAPI アプリケーションとルーティング
│ ├── models/ # Tortoise ORM モデル
│ │ ├── **init**.py
│ │ ├── clients.py
│ │ ├── members.py
│ │ ├── projects.py
│ │ └── ... # その他のモデル
│ ├── schemas/ # Pydantic スキーマ
│ │ ├── **init**.py
│ │ ├── clients.py
│ │ ├── members.py
│ │ ├── projects.py
│ │ └── ... # その他のスキーマ
│ ├── routers/ # ルーティングモジュール
│ │ ├── **init**.py
│ │ ├── clients.py
│ │ ├── members.py
│ │ ├── projects.py
│ │ └── ... # その他のルーター
│ ├── cruds/ # crud モジュール
│ │ ├── **init**.py
│ │ ├── clients.py
│ │ ├── members.py
│ │ ├── projects.py
│ │ └── ... # その他のルーター
│ └── config.py # 設定ファイル（DB 設定含む）
│
├── migrations/ # マイグレーションファイル
├── tests/ # テストケース
├── .env # 環境変数と設定値
├── pyproject.toml # poetry 依存関係と設定
└── README.md # プロジェクトの説明
```

### models

app/models ディレクトリ内に、ER 図に基づいて各テーブルのモデルを定義する。
Tortoise ORM を使うよ
データベースのテーブルをモデル化するためのデータモデル（Tortoise-ORM のモデルなど）を含むディレクトリ。
データベースのテーブルやデータ構造を Python のクラスとして表現し、データベースとの対話やデータの操作を行うためのモデルを定義する。
これらのモデルはデータベースのテーブルと 1 対 1 で対応し、データの取得、作成、更新、削除などの操作を提供する

### schemas

app/schemas ディレクトリ内に、リクエストとレスポンスのデータ構造を定義する
FastAPI のスキーマなので DB スキーマとは別物
リクエストとレスポンスのデータの形式を定義し、データの妥当性を検証するために使用される。
Pydantic スキーマを使用することで、リクエストデータのバリデーションやレスポンスデータのシリアライズ/デシリアライズが行える。

### routers

app/routers ディレクトリ内に、それぞれのモデルに対する CRUD 操作を行うためのルーターを定義する
API のエンドポイントを定義し、リクエストを処理してレスポンスを生成するための FastAPI ルーターを含むディレクトリ。
FastAPI のルーターは、異なるエンドポイントを定義し、リクエストを処理してクライアントに対するレスポンスを生成する

### cruds

ビジネスロジックやデータベース操作を抽象化し、CRUD（作成、読み取り、更新、削除）操作を提供するモジュールを含むディレクトリ。
データベース操作に関連するビジネスロジックを独立したモジュールとして切り出し、データベースの操作をより再利用可能な形で提供する。
CRUD 操作は、モデルとデータベースの間のインターフェースとして機能し、エンドポイント内で利用される。

## poetry コマンド

仮想環境作成
`poetry init`

仮想環境に入る
`poetry shell`

poetry でライブラリのインストール

```
poetry add fastapi
poetry add fastapi-admin
poetry add tortoise-orm
```

poerty で追加したライブラリ達

```
poetry add aiomysql
poetry add aerich
poetry add email-validator
poetry add uvicorn
# MySQLデータベースへの接続時に使用される認証方法
pip install cryptography

開発環境のみで必要ようなライブラリ
poetry add pytest httpx pytest-asyncio --dev

```

仮想環境に入っているか確認

```
echo $VIRTUAL_ENV
/Users/adachikeiichi/Documents/python/python-turorial/fast-api-darkside/.venv
```

## その他

uvicorn で fastapi を起動
`uvicorn app.main:app --reload`

### Tortoise-ORM について

#### Tortoise-ORM と SQLAlchemy の違いとそれぞれの利点

SQLAlchemy
歴史と成熟度: SQLAlchemy は長い歴史を持ち、Python で最も成熟して使用されている ORM の一つです。多くの本番環境での使用実績があります。
同期/非同期サポート: 元々は同期オペレーション用に設計されていますが、SQLAlchemy 1.4 からは非同期サポートが導入され、FastAPI と組み合わせて非同期で使用することができます。
柔軟性と機能性: 高度なクエリ構築、複雑なリレーションシップマッピング、マイグレーションサポート（Alembic を通じて）など、豊富な機能を提供します。

Tortoise-ORM
非同期ネイティブ: Tortoise-ORM は非同期 IO を前提として設計されており、FastAPI などの非同期フレームワークと自然に統合されます。
シンプルでモダン: Django の ORM にインスパイアされた API を持ち、Python の非同期機能とモダンな開発要件に適応しています。
簡潔さと使いやすさ: Tortoise-ORM は使いやすさを重視しており、設定やボイラープレートコードが少ないため、プロジェクトのセットアップがシンプルになります。

今回は高度なデータベース操作は必要ないので、簡単に非同期処理できる Tortoise-ORM を使うんだろう。。

### マイグレーション

Tortoise-ORM では、aerich というマイグレーションツールを使用してマイグレーションを管理し、マイグレーションの履歴を残すことができる。
aerich は Tortoise-ORM のためのマイグレーションツールであり、モデルの変更を追跡し、データベーススキーマのマイグレーションを行うことができるので導入する。
→ なんかエラー発生するのでやめる

### データベース接続情報

将来的には、dotenv ライブラリとか使用して本番・開発で管理する

### 細かいこと

## 問題

fastapi-admin と pytest では distutils が必要になる

python3.12 では標準モジュールの distutils が存在しないため、エラーが発生する
distutils は python プロジェクトのビルド、配布、インストールを容易にする

```
  from distutils.version import StrictVersion
ModuleNotFoundError: No module named 'distutils'
line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
```

エラーが発生する条件： - pytest でエラーが発生する - fastapi-admin でエラーが発生する（aioredis を使用するときにエラーが発生するみたい） - distutils は 非推奨で、Python 3.12 での除去が予定されている
[distutils に関する公式ドキュメント](https://docs.python.org/ja/3.10/library/distutils.html#module-distutils)

対策：バージョン下げる 3.11 系が優秀という記事があったので一旦 3.11 で起動する

python のバージョン下げる方法

```
## 仮想環境に入っている場合は一旦抜ける
deactivate

## 仮想環境を削除
rm -rf .venv/
rm poetry.lock
rm pyproject.toml

## 下記のフォルダにキャッシュが残ってる場合は削除する
## pythonのバージョン変える時はこれ消す（恐らくプロジェクト配下に作成される）
__pycache__

asdf install python 3.10.11

## python3.10.11でpoetryをインストール
pip install poetry

## 仮想環境を作成
poetry init

## 仮想環境に再度入る
poetry shell

## 仮想環境に入ったか一応確認
echo $VIRTUAL_ENV

## 必要なライブラリ再インストール
poetry add fastapi
poetry add fastapi-admin
poetry add tortoise-orm
poetry add aiomysql
poetry add aerich
poetry add email-validator
poetry add uvicorn
.. etc

```

aioredis が python3.11.7 でもサポートされてなかった。。。
aioredis とは：Redis データベースと非同期に通信するためのライブラリです
https://github.com/aio-libs-abandoned/aioredis-py

というわけで別のライブラリを探す。
fastapi-admin の公式では aioredis を使っている
3.11 でもダメかもしれない
https://github.com/fastapi-admin/fastapi-admin/issues/138

fastapi admin が内部的に aioredis を使っていますので
これじゃ無理ー

3.10 系に下げるしかない。

## redis

docker で起動している redis の IP を特定するコマンド

```
 docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' darkside_redis
```

docker 　で起動している redis に入る方法

```
 docker exec -it darkside_redis /bin/bash
 ## レディスCLIを実行する場合
 redis-cli
```

redis cli コマンドのまとめ

参考：https://qiita.com/hatsu/items/a52817364160e0b6bb60

## fastapi-admin 導入後のディレクトリ構成

fastadmi-admin がらみは一旦 admin/配下で行う

```
fast-api-darkside/
│
├── app/
│   ├── __init__.py
│   ├── main.py # FastAPI アプリケーション、ルーティング、FastAPI-Adminのマウント
│   ├── models/ # Tortoise ORM モデル
│   │   ├── __init__.py
│   │   ├── admin.py # FastAPI-Adminで使用するモデル
│   │   └── ... # その他のモデル
│   ├── schemas/ # Pydantic スキーマ
│   │   ├── __init__.py
│   │   └── ... # スキーマ
│   ├── routers/ # ルーティングモジュール
│   │   ├── __init__.py
│   │   └── ... # その他のルーター
│   ├── cruds/ # CRUD モジュール
│   │   ├── __init__.py
│   │   └── ... # CRUD操作
│   ├── admin/ # FastAPI-Admin設定とカスタマイズ
│   │   ├── __init__.py
│   │   ├── main.py # FastAPI-Adminの設定と初期化
│   │   └── resources.py # FastAPI-Adminのリソース
│   │   └── constants.py # FastAPI-Adminのコンテンツ
│   │   └── templates/ # Jinja2 テンプレート
│   │   │    └── ... # HTMLテンプレートファイル
│   │   └── static/ # 静的ファイル
│   │        └── ...# CSS、画像など（今のところ使わない）
│   └── config.py # 設定ファイル（DB設定など）
│
├── migrations/ # マイグレーションファイル(ORMでマイグレーションファイル作り方わからない)
├── tests/ # テスト用のディレクトリ
│   ├── __init__.py # テスト用DBとのセッション（dotenvで定義する）
│   ├── conftest.py # テスト用のフィクスチャ
│   └── ... # その他のテストケース
├── .env # 環境変数と設定値
├── server.py #サーバー起動
├── pyproject.toml # poetry依存関係と設定
├── docker-compose.yaml
└── README.md
```

## 管理画面作る時の参考

公式：
https://fastapi-admin-docs.long2ice.io/reference/

## プロジェクトの概要（予想）

ER 図からどのようなプロジェクトを読み取る

### 全体像

クライアント、プロジェクト、メンバー、プロジェクトの予算と募集枠、メンバーとプロジェクト枠のアサイン、メンバーのコストを管理するアプリ

### 詳細

#### クライアント（clients）

サービスまたはアプリケーションを利用する企業 or 個人を管理する。
各クライアントは一意の ID、名前、登録日時、削除日時を持つ。

#### メンバー（members）

クライアントに所属する従業員と協力者を管理する。
各メンバーは、所属するクライアント ID、名前、メールアドレス、電話番号、登録日時、削除日時

#### メンバーコスト（member_costs）

各メンバーの特定の期間におけるコスト（給与？）を管理する。
期間（開始日〜終了日）、コスト、登録日時、削除日時をもつ。

#### プロジェクト（projects）

クライアントが実施する各プロジェクトを管理する。
プロジェクトはクライアントに紐づき、名前、プロジェクトの開始日と終了日、登録日時、削除日時を持つ。

#### プロジェクト予算（project_budgets）

プロジェクトの特定期間における予算を管理。
期間（開始日〜終了日）、予算額、登録日時、削除日時をもつ。

#### プロジェクト募集枠（project_slots）

プロジェクト内で募集する特定の役割やタスクの枠組みを管理しる。
プロジェクト ID に紐づく、名前、募集枠の開始日と終了日、予算、登録日時、削除日時をもつ。

#### プロジェクトメンバーアサイン（project_member_assigns）

プロジェクトメンバーアサインテーブルは、メンバーがプロジェクトの特定の枠にアサインされることを管理する。プロジェクト枠 ID とメンバー ID に紐づき、アサインの期間（開始日〜終了日）、コスト、登録日時、削除日時を持つ。

## テストについて

pytest を使う、非同期関数をテストする場合は、pytest_asyncio を使うといい感じになる
tests/conftest.py でフィクスチャを定義する（テストを実行する際に必要な前提条件とか環境を設定）

あとは各モデルのテストを作成する

テストカバレッジを計測する方法
pytest の plugin でカバレッジ計測の便利なライブラリ「pytest-cov」を使うとよさそう

![alt text](image.png)

テストで全てのケースが担保されているか確認できる

![alt text](image-1.png)

## Tortoise ORM のマイグレーションについて検討

### 概要

公式 Documents：https://tortoise.github.io/migration.html

Tortoise-ORM でのマイグレーション管理には、Aerich というツールを使用する

Aerich は Tortoise-ORM を追加した時に追加されてる

### Tortoise-ORM の設定ファイルに Aerich を追加する

```
TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456@127.0.0.1:3306/test"},
    "apps": {
        "models": {
            "models": ["yourapp.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

```

### Aerich の初期化

設定ファイルがある path 指定する

```
aerich init -t app.config.db.TORTOISE_ORM
```

### データベースの初期化

```
aerich init-db
```

### モデルの更新とマイグレーションの作成

モデルを更新した後、aerich migrate コマンドを使用してマイグレーションファイル
カラムの削除とか追加とかね

```
aerich migrate --name some_migration_name
```

命名規則

```
_[モデル名]_[操作内容].py
## add_column, remove_column, create_table, drop_table, modify_column など分かるようにする

_client_drop_name_column
```

### マイグレーションの適用

マイグレーションをデータベースに適用する

```
aerich upgrade
```

### マイグレーションの履歴、ダウングレード、その他の操作

```
Aerichでは、マイグレーションの履歴の確認、特定のバージョンへのダウングレード、現在のマイグレーションの状態の確認など、
さまざまな操作がサポートされる。各コマンドの詳細については、aerich -hを参照する。

これらのステップに従うことで、Tortoise-ORMを使用したプロジェクトでマイグレーションを管理できるようになる。

```

## プロジェクトのルールについて

ある程度考える必要がありそう
この辺は別途整理必要
