from fastapi import FastAPI
import itertools
import lorem
import pydantic

app = FastAPI()


class ChatRequest(pydantic.BaseModel):
    msg: str
    api_key: str


@app.get("/")
def root():
    return {"message": "Third Party Service"}


@app.post("/chat")
def chat(req: ChatRequest):
    if req.api_key != "123456":
        return {"message": "Invalid API Key"}
    print(f"Received message: {req.msg}")
    res = list(itertools.islice(lorem.paragraph(sentence_range=(3, 10)), 1))[0]
    return {"message": f"{req.msg}\n{res}"}
