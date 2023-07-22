from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests

app = FastAPI(
    title="zkChat Proxy Server",
    description="This is a proxy server for zkChat.",
)


class ProxyRequest(BaseModel):
    msg: str
    api_key: int


tps_base_url = "http://localhost:10001"


@app.get("/")
def index():
    return RedirectResponse(url="/docs")


@app.post("/tps")
def query_tps(req: ProxyRequest):
    res = requests.post(
        tps_base_url + "/chat",
        json={"msg": req.msg, "api_key": req.api_key},
    )
    return res.json()
