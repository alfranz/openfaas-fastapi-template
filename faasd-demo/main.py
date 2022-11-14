from fastapi import FastAPI, Request
from function.handler import router
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.mount("/assets", StaticFiles(directory="function/assets"), name="assets")

app.include_router(router)
