import asyncio
from faker import Faker
from tortoise import Tortoise, run_async
from tortoise.transactions import in_transaction
from models import (
    Client,
    Project,
    Member,
    ProjectSlot,
    MemberCost,
    ProjectBudget,
    ProjectMemberAssign,
)

fake = Faker("ja_JP")


async def delete_existing_data():
    async with in_transaction() as conn:
        await ProjectMemberAssign.all().using_db(conn).delete()
        await ProjectSlot.all().using_db(conn).delete()
        await MemberCost.all().using_db(conn).delete()
        await ProjectBudget.all().using_db(conn).delete()
        await Project.all().using_db(conn).delete()
        await Member.all().using_db(conn).delete()
        await Client.all().using_db(conn).delete()


async def seed():
    await delete_existing_data()
    # Client
    clients = []
    for _ in range(5):
        client = await Client.create(name=fake.company())
        clients.append(client)

    # Project
    projects = []
    for client in clients:
        for _ in range(2):
            project = await Project.create(
                name=fake.bs(),
                client=client,
                start_date=fake.date_between(start_date="-1y", end_date="today"),
                end_date=fake.date_between(start_date="+1y", end_date="+2y"),
            )
            projects.append(project)

    # Member
    members = []
    for client in clients:
        for _ in range(10):
            member = await Member.create(
                client=client,
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
            )
            members.append(member)

    # ProjectSlot
    for project in projects:
        for _ in range(3):
            await ProjectSlot.create(
                project=project,
                name=fake.job(),
                start_date=fake.date_between(start_date="-1y", end_date="today"),
                end_date=fake.date_between(start_date="+1y", end_date="+2y"),
                budget=int(f"{fake.random.randint(10, 99)}0000"),
            )

    # ProjectBudget
    for project in projects:
        await ProjectBudget.create(
            project=project,
            start_date=fake.date_between(start_date="-1y", end_date="today"),
            end_date=fake.date_between(start_date="+1y", end_date="+2y"),
            budget=int(f"{fake.random.randint(10, 99)}0000"),
        )

    # MemberCost
    for member in members:
        await MemberCost.create(
            member=member,
            start_date=fake.date_between(start_date="-1y", end_date="today"),
            end_date=fake.date_between(start_date="+1y", end_date="+2y"),
            cost=int(f"{fake.random.randint(10, 99)}000"),  # メンバーコストって月給？
        )

    # ProjectMemberAssign
    for member in members:
        project_slot = await ProjectSlot.first()
        if project_slot:
            await ProjectMemberAssign.create(
                project_slot=project_slot,
                member=member,
                start_date=fake.date_between(start_date="-1y", end_date="today"),
                end_date=fake.date_between(start_date="+1y", end_date="+2y"),
                cost=int(f"{fake.random.randint(10, 99)}000"),
            )


# DBは一旦ベタがき
async def main():
    await Tortoise.init(
        db_url="mysql://docker:docker@localhost:33071/database",
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas()
    await seed()


if __name__ == "__main__":
    run_async(main())
