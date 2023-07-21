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


if __name__ == "__main__":
    urls = ["http://127.0.0.1:8000/wait", "http://127.0.0.1:8000/asyncwait"]
    funcs = [sync_get_all, thread_pool]
    run_bench(1000, funcs, urls)
