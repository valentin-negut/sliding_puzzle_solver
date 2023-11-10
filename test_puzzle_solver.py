from puzzle_solver import solve_puzzle, get_directions


def test_specific_initial_state():
    # Define the specific initial state
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

    # Ensure the solution is correct
    solution = solve_puzzle(initial_state)
    directions = get_directions(initial_state, solution)

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

    assert directions == expected_directions

