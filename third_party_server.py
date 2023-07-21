from fastapi import FastAPI
import asyncio
import time
import lorem
import random
import itertools

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Third Party Service"}


@app.post("/chat")
def chat(msg):
    print(f"Received message: {msg}")
    res = list(itertools.islice(lorem.paragraph(sentence_range=(3, 10)), 1))[0]
    return {"message": f"{msg}\n{res}"}
