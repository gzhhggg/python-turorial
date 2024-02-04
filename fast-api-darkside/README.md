# fast_api を使った darkside アプリ作成

## python 関係ない個人メモ(後で消す)

md プレビューショートカット
`cmd + k → v`

## ディレクトリ構想（どうするか検討中）

とりあえず下記で実装してみる
参考：https://zenn.dev/dencyu/articles/a94928b9ce45f7
参考公式：https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#file-structure

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

### models

app/models ディレクトリ内に、ER 図に基づいて各テーブルのモデルを定義する。
Tortoise ORM を使うよ
1 ファイル管理だとゴチャゴチャなりそうな気がするので分ける（SSPP は分けてなかった）

### schemas

app/schemas ディレクトリ内に、リクエストとレスポンスのデータ構造を定義する
FastAPI のスキーマなので DB スキーマとは別物

### routers

app/routers ディレクトリ内に、それぞれのモデルに対する CRUD 操作を行うためのルーターを定義する

## poetry コマンド

仮想環境作成
`petry init`

仮想環境に入る
`poetry shell`

poetry でライブラリのインストール

```
poetry add fastapi
poetry add fastapi-admin
poetry add tortoise-orm
```

poerty で追加したライブラリ達

- aiomysql
- aerich

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
