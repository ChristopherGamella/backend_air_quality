from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class AirQualityBase(BaseModel):
    Date: date
    Time: time
    CO_GT: Optional[float]
    PT08_S1_CO: Optional[float]
    NMHC_GT: Optional[float]
    C6H6_GT: Optional[float]
    PT08_S2_NMHC: Optional[float]
    NOx_GT: Optional[float]
    PT08_S3_NOx: Optional[float]
    NO2_GT: Optional[float]
    PT08_S4_NO2: Optional[float]
    PT08_S5_O3: Optional[float]
    T: Optional[float]
    RH: Optional[float]
    AH: Optional[float]


class AirQualityResponse(AirQualityBase):
    id: int

    class Config:
        from_attributes = True  # Allows ORM models to work with Pydantic


class AirQualityCoGtResponse(BaseModel):
    Date: date
    CO_GT: Optional[float]


class AirQualityColResponse(BaseModel):
    Date: date
    Col: Optional[float]
