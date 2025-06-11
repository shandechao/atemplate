from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.deps import get_db
from app.models.record import Record
from enum import Enum
from sqlalchemy import text


router = APIRouter()

@router.get("/records", tags=["Records"])
async def get_default_records(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Record).limit(20))
    records = result.scalars().all()
    return [
        {
            "id": r.id,
            "name": r.name,
            "category": r.category,
            "value": r.value,
            "quantity": r.quantity,
            "timestamp": r.timestamp.isoformat()
        } for r in records
    ]

@router.get("/records/{limit}", tags=["Records"])
async def get_limited_records(
    limit: int = Path(..., ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Record).limit(limit))
    records = result.scalars().all()
    return [
        {
            "id": r.id,
            "name": r.name,
            "category": r.category,
            "value": r.value,
            "quantity": r.quantity,
            "timestamp": r.timestamp.isoformat()
        } for r in records
    ]


class CategoryEnum(str, Enum):
    stock = "stock"
    option = "option"

@router.get("/records/{category}/aggregate", tags=["Records"])
async def aggregate_records_raw(category: CategoryEnum= Path(...),db: AsyncSession = Depends(get_db)):
    print(category)
    print("xxxxxxx")
    sql = text("""
        SELECT 
            name,
            SUM(quantity) AS total_quantity,
            SUM(value) AS total_value,
            AVG(value) AS avg_value,
            COUNT(*) AS count
        FROM records
        WHERE category = :category
        GROUP BY name
    """)
    result = await db.execute(sql, {"category": category.value})
    rows = result.fetchall()
    return [
        {
            "name": row.name,
            "total_quantity": row.total_quantity,
            "total_value": float(row.total_value),
            "avg_value": float(row.avg_value),
            "count": row.count
        }
        for row in rows
    ]


#5 second bucket
@router.get("/records/{category}/volume_by_window", tags=["Records"])
async def volume_by_window(category: CategoryEnum = Path(...), db: AsyncSession = Depends(get_db)):
    sql = text("""
        SELECT 
            to_timestamp(FLOOR(EXTRACT(EPOCH FROM timestamp) / 5) * 5) AS window_start,
            name,
            SUM(quantity) AS total_quantity
        FROM records
        WHERE category = :category
        GROUP BY window_start, name
        ORDER BY window_start, name
    """)
    result = await db.execute(sql, {"category": category.value})
    rows = result.fetchall()
    return [
        {
            "window_start": row.window_start.isoformat(),
            "name": row.name,
            "total_quantity": row.total_quantity
        }
        for row in rows
    ]

@router.get("/records/{category}/avg_price_by_window", tags=["Records"])
async def avg_price_by_window(category: CategoryEnum = Path(...), db: AsyncSession = Depends(get_db)):
    sql = text("""
        SELECT 
            to_timestamp(FLOOR(EXTRACT(EPOCH FROM timestamp) / 5) * 5) AS window_start,
            name,
            AVG(value) AS avg_price
        FROM records
        WHERE category = :category
        GROUP BY window_start, name
        ORDER BY window_start, name
    """)
    result = await db.execute(sql, {"category": category.value})
    rows = result.fetchall()
    return [
        {
            "window_start": row.window_start.isoformat(),
            "name": row.name,
            "avg_price": float(row.avg_price)
        }
        for row in rows
    ]

@router.get("/records/{category}/vwap_by_window", tags=["Records"])
async def vwap_by_window(category: CategoryEnum = Path(...), db: AsyncSession = Depends(get_db)):
    sql = text("""
        SELECT 
            to_timestamp(FLOOR(EXTRACT(EPOCH FROM timestamp) / 5) * 5) AS window_start,
            name,
            ROUND(SUM(value * quantity) / NULLIF(SUM(quantity), 0), 2) AS vwap
        FROM records
        WHERE category = :category
        GROUP BY window_start, name
        ORDER BY window_start, name
    """)
    result = await db.execute(sql, {"category": category.value})
    rows = result.fetchall()
    return [
        {
            "window_start": row.window_start.isoformat(),
            "name": row.name,
            "vwap": float(row.vwap)
        }
        for row in rows
    ]