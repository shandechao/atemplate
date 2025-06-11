from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/dbname")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://testUser:testPWD@localhost/dbname")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
