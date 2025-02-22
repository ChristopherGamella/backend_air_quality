from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table
import os
from fastapi.middleware.cors import CORSMiddleware

from app.routes import air_quality

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "*",  # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# MySQL configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "1122")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "airquality")

# Create SQLAlchemy engine
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

air_quality_table = Table(
    'air_quality', metadata, autoload_with=engine
)

# ✅ JSON time-series endpoint for ECharts

app.include_router(air_quality.router)
