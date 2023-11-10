import pytest

from puzzle_solver import solve_puzzle, get_directions, get_user_input


def test_directions_for_specific_input(monkeypatch):
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # Add a specific initial state here
    expected_directions = [
        "left",
        "down",
        "right",
        "up",
        "left",
        "down",
        "right",
        "right",
        "up",
        "left",
        "left",
        "down",
        "right",
        "right",
        "up",
        "left",
        "down",
        "left",
        "up",
        "right",
        "right",
        "down",
        "left",
        "up",
        "left",
        "down",
        "right",
        "right",
    ]

    # Mock user input for get_user_input
    monkeypatch.setattr("builtins.input", lambda _: "1 2 3 4 0 5 6 7 8")

    # Redirect standard output to capture the printed directions
    directions = get_directions(initial_state, solve_puzzle(initial_state))
    assert directions == expected_directions


def test_get_user_input_valid(monkeypatch):
    user_input = "1 2 3 4 5 6 7 8 0"
    expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    assert get_user_input() == expected_output


def test_get_user_input_invalid(monkeypatch):
    user_input = "1 2 3 4 5 6 7 8"  # Missing the last element

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    assert get_user_input() is None


if __name__ == "__main__":
    pytest.main()
