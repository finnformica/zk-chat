from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from fastapi import FastAPI
import requests

app = FastAPI(
    title="zkChat Proxy Server",
    description="This is a proxy server for zkChat.",
)


class History(BaseModel):
    user_messages: list
    bot_messages: list


class ProxyRequest(BaseModel):
    message: str
    history: History
    api_key: int


tps_base_url = "http://localhost:10001"


@app.get("/")
def index():
    return RedirectResponse(url="/docs")


@app.post("/tps")
def query_tps(req: ProxyRequest):
    res = requests.post(
        tps_base_url + "/chat",
        json={
            "message": req.message,
            "history": {
                "user_messages": req.history.user_messages,
                "bot_messages": req.history.bot_messages,
            },
            "api_key": req.api_key,
        },
    )
    return res.json()
