# tests/test_app.py
from src.app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Harness CI/CD!' in response.data
