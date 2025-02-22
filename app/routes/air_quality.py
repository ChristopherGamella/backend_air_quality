from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import air_quality_table
from ..schemas import AirQualityResponse, AirQualityColResponse
from ..database import get_db
from datetime import date

router = APIRouter()


def with_date_filter(query, start_date, end_date, db):
    if start_date:
        query = query.filter(air_quality_table.c.Date >= start_date)
    if end_date:
        query = query.filter(air_quality_table.c.Date <= end_date)

    return query.all()


@router.get("/aq", response_model=List[AirQualityResponse])
async def get_air_quality(db: Session = Depends(get_db)):
    query = select(air_quality_table)
    results = db.execute(query).fetchall()
    return [dict(row._mapping) for row in results]


@router.get("/aq/CO_GT", response_model=list[AirQualityColResponse])
async def read_grouped_CO_GT(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.CO_GT), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/PT08_S1_CO", response_model=list[AirQualityColResponse])
async def read_grouped_PT08_S1_CO(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.PT08_S1_CO), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/PT08_S2_NMHC", response_model=list[AirQualityColResponse])
async def read_grouped_PT08_S2_NMHC(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.PT08_S2_NMHC), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/NMHC_GT", response_model=list[AirQualityColResponse])
async def read_grouped_NMHC_GT(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.NMHC_GT), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/C6H6_GT", response_model=list[AirQualityColResponse])
async def read_grouped_C6H6_GT(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.C6H6_GT), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/PT08_S3_NOx", response_model=list[AirQualityColResponse])
async def read_grouped_PT08_S3_NOx(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.PT08_S3_NOx), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/NO2_GT", response_model=list[AirQualityColResponse])
async def read_grouped_NO2_GT(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.NO2_GT), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/PT08_S4_NO2", response_model=list[AirQualityColResponse])
async def read_grouped_PT08_S4_NO2(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.PT08_S4_NO2), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/PT08_S5_O3", response_model=list[AirQualityColResponse])
async def read_grouped_PT08_S5_O3(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.PT08_S5_O3), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/T", response_model=list[AirQualityColResponse])
async def read_grouped_T(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.T), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/RH", response_model=list[AirQualityColResponse])
async def read_grouped_RH(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.RH), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)


@router.get("/aq/AH", response_model=list[AirQualityColResponse])
async def read_grouped_AH(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(
        None, description="Start date for filtering"),
    end_date: Optional[date] = Query(
        None, description="End date for filtering")
):
    query = db.query(
        air_quality_table.c.Date,
        func.round(func.avg(air_quality_table.c.AH), 3).label('Col')
    ).group_by(air_quality_table.c.Date)

    return with_date_filter(query, start_date, end_date, db)
