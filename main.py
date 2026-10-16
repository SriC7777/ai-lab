from typing import Annotated

import requests
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from weather import get_weather

app = FastAPI(title="Weather API")


class Weather(BaseModel):
    latitude: float
    longitude: float
    temperature_c: float
    windspeed_kmh: float


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/weather", response_model=Weather)
def weather(
    lat: Annotated[float, Query(ge=-90, le=90)],
    lon: Annotated[float, Query(ge=-180, le=180)],
) -> Weather:
    try:
        w = get_weather(lat, lon)
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Weather service unavailable")
    return Weather(
        latitude=lat,
        longitude=lon,
        temperature_c=w["temperature"],
        windspeed_kmh=w["windspeed"],
    )