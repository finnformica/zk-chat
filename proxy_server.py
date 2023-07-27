from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.config import Config
from pydantic import BaseModel
from fastapi import FastAPI
import requests
import json

app = FastAPI(
    title="zkChat Proxy Server",
    description="This is a proxy server for zkChat.",
)
app.add_middleware(SessionMiddleware, secret_key="!secret")

config = Config(".env")
oauth = OAuth()

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth.register(
    name="google",
    client_id=config("GOOGLE_CLIENT_ID"),
    client_secret=config("GOOGLE_CLIENT_SECRET"),
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)


class History(BaseModel):
    user_messages: list
    bot_messages: list


class ProxyRequest(BaseModel, Request):
    message: str
    history: History
    api_key: int


tps_base_url = "http://localhost:10001"


@app.get("/")
async def homepage(request: Request):
    user = request.session.get("user")
    if user:
        data = json.dumps(user)
        html = f"<pre>{data}</pre>" '<a href="/logout">logout</a>'
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")


@app.post("/tps")
def query_tps(request: ProxyRequest):
    user = request.session.get("user")
    if user:
        res = requests.post(
            tps_base_url + "/chat",
            json={
                "message": request.message,
                "history": {
                    "user_messages": request.history.user_messages,
                    "bot_messages": request.history.bot_messages,
                },
                "api_key": request.api_key,
            },
        )
        return res.json()
    else:
        return {"error": "not logged in"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=8000)
