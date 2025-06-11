import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
##load_dotenv(dotenv_path=Path().resolve() / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")


ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")


engine = create_async_engine(
    ASYNC_DATABASE_URL, 
    echo=True,  
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()