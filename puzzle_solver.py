import heapq
import copy


class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        # Manhattan distance heuristic
        h = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    h += abs(i - goal_i) + abs(j - goal_j)
        return h


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(node.state)
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, parent=node, move=(ni, nj)))
    return neighbors


def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]


def solve_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_node)

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor not in closed_set and neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

    return None  # No solution found


def print_puzzle(state):
    for row in state:
        print(row)


def main():
    # Example usage:
    initial_state = [[6, 8, 7], [1, 3, 5], [4, 2, 0]]
    print("Initial State:")
    print_puzzle(initial_state)

    solution = solve_puzzle(initial_state)

    if solution:
        print("\nSolution Steps:")
        current_state = copy.deepcopy(initial_state)
        print_puzzle(current_state)

        for move in solution:
            ni, nj = move
            i, j = get_blank_position(current_state)
            current_state[i][j], current_state[ni][nj] = current_state[ni][nj], current_state[i][j]
            print("\nMove blank:", move)
            print_puzzle(current_state)
    else:
        print("\nNo solution found.")


if __name__ == "__main__":
    main()
