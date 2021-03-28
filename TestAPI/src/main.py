from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import random


class addition(BaseModel):
    a: int
    b: int


app = FastAPI()

@app.get("/random")
async def randomNum(testQueryParam: str):
    return {"number": random.randint(1, 11), "testParam": testQueryParam}

@app.post("/add")
async def add(item: addition):
    return {"answer": item.a + item.b}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5002)
