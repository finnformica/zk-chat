from fastapi import FastAPI
import time
import asyncio
import requests

app = FastAPI()

tps_base_url = "http://localhost:10001"


@app.get("/")
def root():
    return {"message": "zkChat Proxy Server"}


@app.post("/tps")
def query_tps(msg):
    res = requests.post(tps_base_url + "/chat", json={"msg": msg})
    return res.json()
