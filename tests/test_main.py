from fastapi.testclient import TestClient

from app.main import app

test_client = TestClient(app)


def test_read_root() -> None:
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "EPAM PROJECT START"}


def test_read_item() -> None:
    response = test_client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": "1", "q": ""}
