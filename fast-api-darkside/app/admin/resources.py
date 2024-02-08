import os

from fastapi_admin.app import app
from fastapi_admin.resources import (
    Action,
    Dropdown,
    Field,
    Link,
    Model,
    ToolbarAction,
    displays,
    inputs,
)
from fastapi_admin.widgets.filters import ForeignKey
from .constants import BASE_DIR
from ..models import (
    Admin,
    Client,
    Member,
    Project,
    ProjectSlot,
    ProjectBudget,
    ProjectMemberAssign,
)


@app.register
class Dashboard(Link):
    label = "Dashboard"
    icon = "fas fa-home"
    url = "/admin"


@app.register
class GitHub(Link):
    label = "GitHub"
    icon = "fab fa-github"
    url = "https://github.com/gzhhggg/python-turorial/tree/main/fast-api-darkside/"
    target = "_blank"


# Admin
@app.register
class AdminResource(Model):
    label = "管理者"
    # 管理するTortoise ORMモデルを指定
    model = Admin
    icon = "fas fa-user"
    fields = [
        "id",
        Field(name="username", label="ユーザー名"),
        Field(
            name="password",
            label="パスワード",
            display=displays.InputOnly(),  # リストに表示しない
            input_=inputs.Password(),  # HTML form input typeをpasswordに指定
        ),
        Field(
            name="email",
            label="Email",
            input_=inputs.Email(),  # HTML form input typeをemailに指定
        ),
        "created_at",
    ]


# Client
@app.register
class ClientResource(Model):
    label = "クライアント"
    model = Client
    icon = "fas fa-user-tie"
    fields = [
        "id",
        Field(name="name", label="クライアント名"),
        "created_at",
    ]


# Project
@app.register
class ProjectResource(Model):
    label = "プロジェクト"
    model = Project
    icon = "fas fa-project-diagram"
    fields = [
        "id",
        Field(
            name="client_id",
            label="クライアント",
            input_=inputs.ForeignKey(model=Client),
        ),
        Field(name="name", label="プロジェクト名"),
        Field(name="start_date", label="開始日", input_=inputs.Date()),
        Field(name="end_date", label="終了日", input_=inputs.Date()),
        "created_at",
    ]


# ProjectBudget
@app.register
class ProjectSlotResource(Model):
    label = "プロジェクト期間別予算"
    model = ProjectBudget
    icon = "fas fa-money-bill"
    fields = [
        "id",
        Field(
            name="project_id",
            label="project",
            input_=inputs.ForeignKey(model=Project),
        ),
        Field(name="start_date", label="開始日", input_=inputs.Date()),
        Field(name="end_date", label="終了日", input_=inputs.Date()),
        Field(name="budget", label="予算", input_=inputs.Number()),
        "created_at",
    ]


# ProjectSlot
@app.register
class ProjectSlotResource(Model):
    label = "プロジェクト募集枠"
    model = ProjectSlot
    icon = "fas fa-id-badge"
    fields = [
        "id",
        Field(
            name="project_id",
            label="project",
            input_=inputs.ForeignKey(model=Project),
        ),
        Field(name="name", label="役割"),
        Field(name="start_date", label="募集開始日", input_=inputs.Date()),
        Field(name="end_date", label="募集終了日", input_=inputs.Date()),
        Field(name="budget", label="予算", input_=inputs.Number()),
        "created_at",
    ]


# Member
@app.register
class MemberResource(Model):
    label = "メンバー"
    model = Member
    icon = "fas fa-user-nurse"
    fields = [
        "id",
        Field(
            name="client_id",
            label="Client",
            input_=inputs.ForeignKey(model=Client),
        ),
        "name",
        Field(name="email", input_=inputs.Email()),
        "phone",
        "created_at",
    ]


# ProjectMemberAssign
@app.register
class ProjectMemberAssignResource(Model):
    label = "プロジェクトメンバーアサイン"
    model = ProjectMemberAssign
    icon = "fas fa-user-check"
    fields = [
        "id",
        Field(
            name="project_slot_id",
            label="project_slot",
            input_=inputs.ForeignKey(model=ProjectSlot),
        ),
        Field(
            name="member_id",
            label="member",
            input_=inputs.ForeignKey(model=Member),
        ),
        Field(name="start_date", label="アサイン開始日", input_=inputs.Date()),
        Field(name="end_date", label="アサイン終了日", input_=inputs.Date()),
        Field(name="cost", label="コスト", input_=inputs.Number()),
        "created_at",
    ]
