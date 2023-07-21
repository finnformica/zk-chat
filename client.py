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


def post(url, worker_no):
    resp = requests.post(
        url, json={"msg": f"Hello chatbot! I am worker {worker_no}", "api_key": 123456}
    )
    assert resp.status_code == 200, print(f"Worker {worker_no} failed to process")

    print(f"Worker {worker_no} finished processing")
    return resp.json()


def thread_pool(url, n, limit=None):
    limit_ = limit or n
    with Pool(max_workers=limit_) as pool:
        result = pool.map(post, [url] * n, range(n))
    return result


if __name__ == "__main__":
    url = "http://localhost:10000/tps"
    thread_pool(url, 10)
