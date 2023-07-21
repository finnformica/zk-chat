import asyncio
import aiohttp
import functools
import time

import requests
from concurrent.futures import ThreadPoolExecutor as Pool


def timed(N, url, fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        print(f"{N / duration:.2f} reqs / sec | {N} reqs | {url} | {fn.__name__}")
        return res

    return wrapper


def get(url):
    resp = requests.get(url)
    assert resp.status_code == 200
    return resp.json()


def sync_get_all(url, n):
    l = [get(url) for _ in range(n)]
    return l


def run_bench(n, funcs, urls):
    for url in urls:
        for func in funcs:
            timed(n, url, func)(url, n)


def thread_pool(url, n, limit=None):
    limit_ = limit or n
    with Pool(max_workers=limit_) as pool:
        result = pool.map(get, [url] * n)
    return result


async def aget(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        json = await response.json()
        return json


async def gather_limit(n_workers, *tasks):
    semaphore = asyncio.Semaphore(n_workers)

    async def sem_task(task):
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def aget_all(url, n, n_workers=None):
    limit = n_workers or n
    async with aiohttp.ClientSession() as session:
        result = await gather_limit(limit, *[aget(session, url) for _ in range(n)])
        return result


def async_main(url, n):
    return asyncio.run(aget_all(url, n))


if __name__ == "__main__":
    urls = ["http://127.0.0.1:8000/wait", "http://127.0.0.1:8000/asyncwait"]
    funcs = [sync_get_all, thread_pool, async_main]
    run_bench(100, funcs, urls)
    run_bench(1000, [thread_pool, async_main], urls)
