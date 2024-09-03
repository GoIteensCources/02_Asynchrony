import asyncio
import time

from fastapi import FastAPI
import httpx
import requests
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/asleep")
async def async_sleep():
    await asyncio.sleep(2)
    return {"message": "Асинхронна відповідь після 10 секунди очікування"}


@app.get("/sleep")
def sync_sleep():
    time.sleep(2)
    return {"message": "Cинхронна відповідь після 10 секунди очікування"}


@app.get("/query")
def get_query():
    return {"message": "Hello from query"}


@app.get("/get_wiki/")
async def get_wiki_page():
    url = "https://uk.wikipedia.org/wiki/Python"
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)

    return HTMLResponse(response.text)
