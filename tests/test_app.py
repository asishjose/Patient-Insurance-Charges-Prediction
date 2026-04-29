import pytest
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from App.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_api(client):
    payload = {
        "age": 30, "sex": "male", "bmi": 25.0,
        "children": 1, "smoker": "no", "region": "southwest"
    }
    response = client.post("/predict_api",
                           json=payload,
                           content_type="application/json")
    assert response.status_code == 200
