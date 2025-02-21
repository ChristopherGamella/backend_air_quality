from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from ..models import air_quality_table
from ..schemas import AirQualityResponse
from ..database import get_db

router = APIRouter()


@router.get("/air_quality", response_model=List[AirQualityResponse])
async def get_air_quality(db: Session = Depends(get_db)):
    query = select(air_quality_table)
    results = db.execute(query).fetchall()
    return [dict(row._mapping) for row in results]
