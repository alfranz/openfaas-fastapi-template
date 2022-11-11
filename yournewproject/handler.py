from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="function/assets")

class TemperatureResponse(BaseModel):
    temperature: float = 21.0
    location: str = "Berlin, Germany"


@router.get("/")
async def service_index(request: Request):
    return templates.TemplateResponse(
        "index.jinja",
        {"request": request, "a_variable": "hello this is arbitrary text"},
    )

@router.get("/temperature")
async def temp_endpoint(response_class=TemperatureResponse):
    return TemperatureResponse()