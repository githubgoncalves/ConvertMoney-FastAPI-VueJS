import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

@pytest.mark.slow
def test_convert():
    response = client.get("http://localhost:5000/api/convert-currency?from_=USD&to_=BRL&amount_=1")
    assert response.status_code == 200