from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import itertools
import lorem


app = FastAPI(
    title="Third Party Service",
    description="This is a third party service for zkChat.",
)


class ChatRequest(BaseModel):
    msg: str
    api_key: int


@app.get("/")
def index():
    return RedirectResponse(url="/docs")


@app.post("/chat")
def chat(req: ChatRequest):
    if req.api_key != 123456:
        return {"message": "Invalid API Key"}
    print(f"Received message: {req.msg}")
    res = list(itertools.islice(lorem.paragraph(sentence_range=(3, 10)), 1))[0]
    return {"message": f"{req.msg}\n{res}"}
