# backend/insert_demo_data.py

# backend/app/scripts/insert_demo_data.py

import asyncio
from datetime import datetime, timedelta,timezone
from random import choice, randint, uniform

from sqlalchemy import text
from app.core.database import engine  # ✅ 复用项目已有 engine


"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import async_session 
async def clear_db():
    async with async_session() as session:
        await session.execute(text("TRUNCATE TABLE records RESTART IDENTITY CASCADE;"))
        await session.commit()

clear_db()
"""

async def insert_data():

    symbols = ['AAPL', 'TSLA', 'MSFT', 'GOOG', 'AMZN']
    categories = ['stock', 'option']
    base_time = datetime.utcnow().replace(tzinfo=None)

    sql = text("""
        INSERT INTO records (name, category, value, quantity, timestamp)
        VALUES (:name, :category, :value, :quantity, :timestamp)
    """)

    async with engine.begin() as conn:
        for i in range(50):
            stock = choice(symbols)
            category = choice(categories);
            price = round(uniform(100, 300), 2)
            quantity = randint(1, 100)
            timestamp = base_time + timedelta(seconds=i * 2)

            await conn.execute(sql, {
                "name": stock,
                "category": category,  
                "value": price,
                "quantity": quantity,
                "timestamp": timestamp
            })

    print("✅ success insert 50 random record")

if __name__ == "__main__":
    asyncio.run(insert_data())