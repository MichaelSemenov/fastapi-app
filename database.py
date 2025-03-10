from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
#async_sessionmaker - нужен для создания сессий для транзакций
#engine - драйвер, движок

engine = create_async_engine (
    "sqlite+aiosqlite:///tasks.db" #База данных+драйвер:///[путь к самой бд ]
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TasksORM(Model):
    __tablename__ = "tasks"
    id: Mapped[int] =mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]] 

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
