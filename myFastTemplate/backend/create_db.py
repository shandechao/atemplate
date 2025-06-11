import asyncio
from app.core.database import engine, Base
from app.models import record
from sqlalchemy import text


async def create_tables():
    async with engine.begin() as conn:
        await conn.execute(text("DROP TABLE IF EXISTS records;"))
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())