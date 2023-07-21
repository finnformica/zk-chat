from concurrent.futures import ThreadPoolExecutor as Pool
import requests


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
