from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname("zk-chat")))
from proxy_server import app


client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200


# @pytest.mark.anyio
# async def test_proxy():
#     async with AsyncClient(app=app) as aclient:
#         response = await aclient.post("example.com", json={"scheme": "https"})
#         assert response.status_code == 200


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
