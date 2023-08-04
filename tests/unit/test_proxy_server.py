from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname("zk-chat"))
from proxy_server import app


client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200


def test_proxy():
    with TestClient(app) as tclient:
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
            },
        }
        response = tclient.post(
            "api.restful-api.dev/objects?scheme=https", json=payload
        )

        assert response.json()["data"] == payload["data"]
        assert response.json()["name"] == payload["name"]
        assert response.status_code == 200
