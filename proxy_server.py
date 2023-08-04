from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from contextlib import asynccontextmanager
from starlette.requests import Request
from starlette.config import Config
from pydantic import BaseModel
from fastapi import FastAPI
import httpx
import json


@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialise the client on startup and add it to the state
    async with httpx.AsyncClient() as client:
        yield {"client": client}
        # client closes on shutdown


app = FastAPI(
    lifespan=lifespan,
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


@app.post("/{path:path}")
async def proxy(request: Request, path: str, scheme: str = "http"):
    url = f"{scheme}://{path}"
    payload = await request.json()
    client = request.state.client
    response = await client.post(url, params=request.query_params, json=payload)

    return response.json()
