from concurrent.futures import ThreadPoolExecutor as Pool
from lorem import sentence
import itertools
import requests
import random
import json
import time


CHAT_DELAY = (1, 10)
CHAT_LENGTH = (1, 4)
NUM_WORKERS = 10

TPS_API_KEY = 123456


class User:
    def __init__(self, number, url):
        self.worker_no = number
        self.url = url
        self.message = f"Hello chatbot! I am worker {self.worker_no}"
        self.api_key = TPS_API_KEY
        self.history = {
            "user_messages": [],
            "bot_messages": [],
        }

    def generate_chat(self):
        return list(itertools.islice(sentence(), 1))[0]

    def request_proxy(self):
        res = requests.post(
            self.url,
            json={
                "message": self.generate_chat(),
                "history": self.history,
                "api_key": self.api_key,
            },
        )

        assert res.status_code == 200, print(
            f"Worker {self.worker_no} failed to process"
        )
        self.history = res.json()["history"]

        return res.json()


def post(url, worker_no):
    user = User(worker_no, url)
    for i in range(random.randint(*CHAT_LENGTH)):
        time.sleep(random.randint(*CHAT_DELAY))
        user.request_proxy()

    return user.history


def thread_pool(url, num_workers, limit=None):
    limit_ = limit or num_workers
    with Pool(max_workers=limit_) as pool:
        result = pool.map(post, [url] * num_workers, range(num_workers))
    return result


if __name__ == "__main__":
    url = "http://localhost:10000/tps"
    result = thread_pool(url, NUM_WORKERS)

    for i, res in enumerate(result):
        print(f"Worker {i}:\n{json.dumps(res['history'], indent=2)}\n")
