from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import itertools
from lorem import paragraph


app = FastAPI(
    title="Third Party Service",
    description="This is a third party service for zkChat.",
)


class History(BaseModel):
    user_messages: list
    bot_messages: list


class ChatRequest(BaseModel):
    message: str
    history: History
    api_key: int


@app.get("/")
def index():
    return RedirectResponse(url="/docs")


@app.post("/chat")
def chat(req: ChatRequest):
    if req.api_key != 123456:
        return {"message": "Invalid API Key"}

    res = list(itertools.islice(paragraph(sentence_range=(3, 10)), 1))[0]

    user_messages = (req.history.user_messages or []) + [req.message]
    bot_messages = (req.history.bot_messages or []) + [res]

    return {
        "message": res,
        "history": {
            "user_messages": user_messages,
            "bot_messages": bot_messages,
        },
    }
