from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import random

router = APIRouter()
templates = Jinja2Templates(directory="assets")


class TemperatureResponse(BaseModel):
    temperature: float = 21.0
    location: str = "Berlin, Germany"


@router.get("/")
async def service_index(request: Request):
    random_int = random.randint(0, 100)
    return templates.TemplateResponse(
        "index.jinja",
        {"request": request, "variable": random_int},
    )


@router.get("/temperature")
async def temp_endpoint(response_class=TemperatureResponse):
    return TemperatureResponse()
