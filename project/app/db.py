import os

# Old way of import sync session
# from sqlmodel import create_engine, SQLModel, Session
from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine

from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")

# Old way to create sync engine
# engine = create_engine(DATABASE_URL, echo=True)

# new way to create async engine
engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))


# Old Sync way to create all table
# def init_db():
#     SQLModel.metadata.create_all(engine)

# New Async way to create all tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# Old Sync way to get session
# def get_session():
#     with Session(engine) as session:
#         yield session

# New Async way to create session
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
