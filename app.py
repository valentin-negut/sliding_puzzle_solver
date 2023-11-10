from flask import Flask, render_template, request
from puzzle_solver import solve_puzzle, get_directions

app = Flask(__name__)


def group_items(items, group_size):
    return [items[i : i + group_size] for i in range(0, len(items), group_size)]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = parse_input(request.form["user_input"])
        if user_input is not None:
            solution = solve_puzzle(user_input)
            if solution:
                directions = get_directions(user_input, solution)
                grouped_directions = group_items(directions, 4)
                return render_template("solution.html", initial_state=user_input, solution=grouped_directions)
            else:
                return render_template("error.html", message="No solution found.")
        else:
            return render_template("error.html", message="Invalid input. Please provide exactly 9 numbers.")
    return render_template("index.html")


def parse_input(user_input):
    try:
        user_input = [int(num) for num in user_input]
        if len(user_input) == 9:
            return [user_input[i : i + 3] for i in range(0, 9, 3)]
    except ValueError:
        pass
    return None


if __name__ == "__main__":
    app.run()
