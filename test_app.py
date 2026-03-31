import pytest
from unittest import mock
import patch
import json
from app import app
import app as myapp

@pytest.fixture
def client():
    app.config.update({'TESTING': True})
    return app.test_client()

@pytest.fixture
def runner(test_app):
    return test_app.test_cli_runner()

@mock.patch('app.psycopg2.connect')
def test_get_authors( mock_connect):
    expected = [("George Orwell",)]
    mock_conn = mock_connect.return_value
    mock_conn.__enter__.return_value = mock_conn
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.__enter__.return_value = mock_cursor
    mock_cursor.fetchall.return_value = expected
    result = myapp.get_authors()
    assert result == ["George Orwell"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {"Status": "OK"}


def test_ready(client):
    response = client.get("/ready")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {"Status": "Ready"}




