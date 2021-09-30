import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_echo(client):
    res = client.post('/echo', data={'name': 'james', 'age': 17})
    data = res.json
    assert res.status_code == 200
    assert data['name'] == 'james'
    assert data['age'] == '17'
