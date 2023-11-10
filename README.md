# 3x3 Sliding Puzzle Solver

## Overview

This Python program aims to solve the classic 3x3 sliding puzzle using the A* algorithm. The puzzle consists of a 3x3 grid with eight numbered tiles and one blank space, and the goal is to rearrange the tiles into numerical order by sliding them into the empty space.

## Features

- A* algorithm with the Manhattan distance heuristic.
- Displays step-by-step directions to solve.
- Supports custom initial puzzle states.

## Usage

### Prerequisites

- Python 3.x
- Flask

### Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/valentin-negut/sliding_puzzle_solver.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sliding_puzzle_solver
    ```

3. Run the program:

    ```bash
    python app.py
    ```


## Program Explanation

### Simple Explanation

The program uses the A* algorithm to find the optimal solution to the sliding puzzle. The `PuzzleNode` class represents the state of the puzzle at each step. It explores possible moves and chooses the most promising ones based on a heuristic (Manhattan distance).

The `solve_puzzle` function takes the initial state of the puzzle and returns a list of moves to solve it.

### Technical Explanation

- The `PuzzleNode` class encapsulates the state of the puzzle, including the current configuration, the parent node, the move that led to this state, and the cost of reaching this state.

- The `heuristic` function calculates the Manhattan distance, providing an estimate of how close the current state is to the goal.

- The `get_neighbors` function generates possible moves from the current state.

- The `solve_puzzle` function uses the A* algorithm to find the optimal path. The open set is a priority queue, and at each step, the algorithm explores the node with the lowest cost.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details.
