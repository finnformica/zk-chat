from authlib.integrations.starlette_client import OAuth, OAuthError

from starlette.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.config import Config

from fastapi import FastAPI, Security
from fastapi_resource_server import OidcResourceServer

from contextlib import asynccontextmanager
from pydantic import BaseModel

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

# BASE_URL = "http://localhost:8080/realms/vc-authn"
BASE_URL = "https://vcauthn-kc.cloudcompass.ca/auth/realms/vc-authn"
CONF_URL = f"{BASE_URL}/.well-known/openid-configuration"
CLIENT_ID = "vue-fe"
PRES_REQ_CONF_ID = "verified-email"

oauth.register(
    name="keycloak_sso",
    server_metadata_url=CONF_URL,
    client_id=CLIENT_ID,
    # client_kwargs={"scope": "openid email profile"},
    client_kwargs={"scope": "openid"},
)


auth_scheme = OidcResourceServer(BASE_URL)


class User(BaseModel):
    sub: str
    username: str
    given_name: str
    family_name: str
    email: str


class History(BaseModel):
    user_messages: list
    bot_messages: list


def get_current_user(claims: dict = Security(auth_scheme)):
    print(claims)
    claims.update(username=claims["preferred_username"])
    user = User.model_validate(claims)
    return user


@app.get("/users/me")
def read_current_user(request: Request):
    user = request.session.get("user")
    if user:
        data = json.dumps(user)
        html = (
            f"<pre>{data}</pre>" '<a href="/logout">logout</a></br><a href="/">home</a>'
        )
        return HTMLResponse(html)
    return RedirectResponse(url="/login")


@app.get("/", include_in_schema=False)
async def homepage(request: Request):
    user = request.session.get("user")
    if user:
        html = '<a href="/logout">logout</a></br><a href="/users/me">user</a>'
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.keycloak_sso.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    try:
        print("Awaiting AUTHN TOKEN")
        token = await oauth.keycloak_sso.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/users/me")


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")


@app.post("/{path:path}")
async def proxy(request: Request, path: str, scheme: str = "http"):
    user = request.session.get("user")
    if user:
        url = f"{scheme}://{path}"
        payload = await request.json()
        client = request.state.client
        response = await client.post(url, params=request.query_params, json=payload)

        return response.json()
    else:
        return {"error": "not logged in"}


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)


if __name__ == "__main__":
    main()
