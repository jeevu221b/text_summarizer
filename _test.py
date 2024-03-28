import pytest
from web import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):
    # Home Page
    res = client.get('/')
    assert res.status_code == 200


def test_min_max_length(client):
    data = {
        "text": "",
        "max_length": 3,
        "min_length": 2
    }
    res = client.post('/summarizer', json=data)
    assert res.status_code == 400
    assert b"Text is Empty" in res.data
