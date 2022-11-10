from fastapi import FastAPI, Request
from function.handler import router
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/assets", StaticFiles(directory="/function/html"), name="assets")

app.include_router(router)
