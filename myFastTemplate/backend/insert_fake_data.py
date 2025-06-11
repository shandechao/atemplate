# backend/insert_demo_data.py

import asyncio
from datetime import datetime, timedelta,timezone

from random import choice, randint, uniform

from app.core.database import AsyncSessionLocal
from app.models.record import Record  # 你的模型路径

async def insert_fake_data():
    categories = ['stock', 'option', 'future']
    base_time = datetime.now(timezone.utc)

    async with AsyncSessionLocal() as session:
        for i in range(50):
            record = Record(
                category=choice(categories),
                value=round(uniform(100, 200), 2),
                quantity=randint(1, 100),
                timestamp=base_time + timedelta(seconds=i * 2)
            )
            session.add(record)
        await session.commit()
        print("✅ 插入完成，共 50 条记录")

if __name__ == "__main__":
    asyncio.run(insert_fake_data())