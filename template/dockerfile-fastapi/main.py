from fastapi import FastAPI, Request
from function.handler import router
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.mount("/assets", StaticFiles(directory="function/assets"), name="assets")

app.include_router(router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    root_path = request.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title="API",
    )