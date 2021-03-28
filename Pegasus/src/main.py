from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import aiohttp
import asyncio
import uvicorn
import pathlib 
import logging



# STATIC PATHS
CWD = pathlib.Path(__file__).resolve().parent
TEMPLATES_PATH = CWD / "templates/"
RESOURCE_PATH = CWD / "static/"
TMP_GATEWAY_ADDR = "http://127.0.0.1:8000"

app = FastAPI()
app.mount("/static", StaticFiles(directory=RESOURCE_PATH), name="static")
templates = Jinja2Templates(directory=TEMPLATES_PATH)

logger = logging.getLogger("app")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
        
@app.get("/gateway/{api}")
async def index(api: str, request: Request):
    query_params = request.query_params
    #logger.error(f"Request for {api}\n{query_params.keys()}")
    msg = {}

    async with aiohttp.ClientSession() as session:
        async with session.get(TMP_GATEWAY_ADDR + "/get/" + api) as resp:
             msg = await resp.json()
             
    return msg


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=5000, log_level="debug")
