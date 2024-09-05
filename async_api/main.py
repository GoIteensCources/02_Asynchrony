import asyncio
import time
import uvicorn

from fastapi import FastAPI, HTTPException, Response
import httpx

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status

# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates


app = FastAPI(debug=True)
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.get("/asleep")
async def async_sleep():
    await asyncio.sleep(10)
    return {"message": "Асинхронна відповідь після 10 секунди очікування"}


@app.get("/sleep")
def sync_sleep():
    time.sleep(10)
    return {"message": "Cинхронна відповідь після 10 секунди очікування"}


@app.get("/query")
async def get_query():
    return {"message": "Hello from query"}


@app.get("/get_wiki/")
async def get_wiki_page():
    url = "https://uk.wikipedia.org/wiki/Python"
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)
    return HTMLResponse(response.text)


users = []


@app.get("/get_users/")
async def get_all_users():
    return {"users": users}


@app.post("/get_users/{name}")
async def add_user(name: str, response: Response):
    if name in users:
        raise HTTPException(status_code=400, detail=f"Name '{name}' is exists")
    users.append(name)
    response.status_code = status.HTTP_201_CREATED
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
