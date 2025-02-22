from sqlalchemy import create_engine, text, Column, String, Float, Integer, Index, MetaData, Table
import pandas as pd
import os
from app.models import air_quality_table, metadata

from dotenv import load_dotenv

load_dotenv()

# MySQL configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "1122")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "airquality")
CSV_FILE = os.getenv("CSV_FILE", "AirQualityUCI.csv")

# Create SQLAlchemy engine
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
engine = create_engine(DATABASE_URL)


def create_table_and_import_data():

    print("Creating table and importing data from CSV file...")
    metadata.create_all(engine)

    try:
        # Create the table if it doesn't exist
        metadata.create_all(engine)

        with engine.connect() as conn:
            result = conn.execute(text(
                "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'air_quality'"))
            table_exists = result.scalar() > 0

            if table_exists:
                result = conn.execute(text("SELECT COUNT(*) FROM air_quality"))
                row_count = result.scalar()
                if row_count > 0:
                    print(
                        "Table 'air_quality' already exists and is not empty. Skipping CSV import.")
                    return True

        # Import data from CSV
        df = pd.read_csv(CSV_FILE, sep=";", decimal=",")

        df = df.dropna(axis=1, how='all')  # Removes empty columns
        df = df.loc[:, ~df.columns.str.contains('Unnamed', case=False)]

        # Rename columns
        df.columns = df.columns.str.replace(
            r'[^a-zA-Z0-9]+', '_', regex=True).str.replace(r'_+$', '', regex=True)

        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y").dt.date
        df["Time"] = pd.to_datetime(df["Time"], format="%H.%M.%S").dt.time

        df = df.dropna(subset=["Date"])
        df = df.where(pd.notnull(df), None)

        df.to_sql("air_quality", con=engine, if_exists="append",
                  index=False, method="multi", chunksize=200)

        print("Done")

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    create_table_and_import_data()
