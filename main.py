from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.exc import SQLAlchemyError
import os
import pandas as pd

from app.routes import air_quality

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

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


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Air Quality API! Auto-reload is enabled."}


@app.get("/timeseries/{column}")
async def get_timeseries(column: str, start_date: str = None, end_date: str = None):
    """Fetches time-series data in JSON format for ECharts"""

    try:
        with engine.connect() as conn:
            query = select(
                air_quality_table.c.Date,
                air_quality_table.c.Time,
                air_quality_table.c[column]
            )

            if start_date and end_date:
                query = query.where(
                    (air_quality_table.c.Date >= start_date) &
                    (air_quality_table.c.Date <= end_date)
                )

            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=[
                              "Date", "Time", column])

            # Convert Date and Time to a single timestamp
            df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
            df = df[["Datetime", column]]

            # Convert data to list of [timestamp, value] pairs
            data = df.values.tolist()

            return {"series": data}

    except SQLAlchemyError as err:
        return {"message": f"Something went wrong: {err}"}
