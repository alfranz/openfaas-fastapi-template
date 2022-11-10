from fastapi import HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List
from fastapi.responses import HTMLResponse, JSONResponse


router = APIRouter()
templates = Jinja2Templates(directory="/function/html")

class ResponseModel(BaseModel):
    data: Dict


@router.get("/", response_model=HTMLResponse)
async def service_index():
    return templates.TemplateResponse("index.jinja", a_variable="hello this is arbitrary text")

