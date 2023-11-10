import pytest

from app import app, parse_input


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")
    assert b"3x3 Sliding Puzzle Solver" in response.data


def test_parse_input_valid():
    user_input = "123456780"
    result = parse_input(user_input)
    assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def test_parse_input_invalid():
    user_input = "12345678"  # Missing the last digit
    result = parse_input(user_input)
    assert result is None

