import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.route("/")
def index():
    return "<h1>zkChat proxy</h1>"


@app.get("/wait")
def wait():
    duration = 0.05
    time.sleep(duration)
    return {"duration": duration}


@app.get("/asyncwait")
async def asyncwait():
    duration = 0.05
    await asyncio.sleep(duration)
    return {"duration": duration}


@app.get("/fib/{n}")
def fib(n: int):
    return {"fib": fibo(n)}


def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
