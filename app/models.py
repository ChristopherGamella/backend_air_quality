from sqlalchemy import Column, Integer, String, Float, Date, Time, MetaData, Table, Index
from .database import engine

metadata = MetaData()

air_quality_table = Table(
    'air_quality', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('Date', Date, nullable=True),
    Column('Time', Time, nullable=True),
    Column('CO_GT', Float),
    Column('PT08_S1_CO', Float),
    Column('NMHC_GT', Float),
    Column('C6H6_GT', Float),
    Column('PT08_S2_NMHC', Float),
    Column('NOx_GT', Float),
    Column('PT08_S3_NOx', Float),
    Column('NO2_GT', Float),
    Column('PT08_S4_NO2', Float),
    Column('PT08_S5_O3', Float),
    Column('T', Float),
    Column('RH', Float),
    Column('AH', Float),
    Index('idx_date', 'Date'),
    Index('idx_time', 'Time')
)
