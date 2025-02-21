from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration from .env
DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://root:1122@mysql/airquality")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
