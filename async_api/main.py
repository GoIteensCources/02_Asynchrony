from fastapi import FastAPI

app = FastAPI(debug=True)

names = list()


@app.get("/names")
async def read_names():
    return {"names": names}


@app.post("/names/{name}")
async def add_name(name: str):
    names.append(name)
    return f"Name '{name}' is added to DB"
