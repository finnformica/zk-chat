from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname("zk-chat")))
from third_party_server import app


client = TestClient(app)


def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
