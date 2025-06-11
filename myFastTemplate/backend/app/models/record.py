
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base
from datetime import datetime, timezone

class Record(Base):
    __tablename__ = "records"  # 表名为 records

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)         #stock name
    category = Column(String, index=True)  # 可对应股票 symbol、分类等
    value = Column(Float)                  # 可对应价格
    quantity = Column(Integer)            # 可对应成交量等
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))