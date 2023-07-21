from fastapi import FastAPI
import requests

app = FastAPI()

tps_base_url = "http://localhost:10001"


@app.get("/")
def root():
    return {"message": "zkChat Proxy Server"}


@app.post("/tps")
def query_tps(msg="Hello chatbot!", api_key=123456):
    res = requests.post(
        tps_base_url + "/chat",
        json={"msg": msg, "api_key": api_key},
    )
    return res.json()
