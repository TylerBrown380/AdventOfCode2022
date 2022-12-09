'''Happy Linter'''
from math import prod

def three_dimensional_array(
    rows: int, columns: int, element_size: int
) -> list[list[list[int]]]:
    '''Happy Linter'''
    return [
        [[0 for _ in range(element_size)] for _ in range(columns)] for _ in range(rows)
    ]

def open_input():
    '''Happy Linter'''
    return open("input.txt", "r", encoding="utf-8").read()

def array_grid(grid):
    '''Happy Linter'''
    n = grid.find("\n")
    return [list(map(int, str(x))) for x in grid.splitlines()]

def part_one(grid: str) -> int:
    '''Happy Linter'''
    n = grid.find("\n")
    interior_grid_size = (n - 2) ** 2
    perimeter_length = n**2 - interior_grid_size
    visible = perimeter_length
    array = [list(map(int, str(x))) for x in grid.splitlines()]
    interior_range = range(1, n - 1)
    for y in interior_range:
        for x in interior_range:
            up = max(col[x] for col in array[:y])
            left = max(array[y][:x])
            down = max(col[x] for col in array[y + 1 :])
            right = max(array[y][x + 1 :])
            current_position = array[y][x]
            if any(current_position > quadrant for quadrant in [up, left, down, right]):
                visible += 1
    return visible

def part_two(grid: str) -> list:
    '''Happy Linter'''
    n = grid.find("\n")
    array = [list(map(int, str(x))) for x in grid.splitlines()]
    interior_range = range(1, n - 1)
    scenic_scores = three_dimensional_array(n - 2, n - 2, 4)
    for x in interior_range:
        for y in interior_range:
            up = list(reversed([col[y] for col in array[:x]]))
            left = list(reversed(array[x][:y]))
            down = [col[y] for col in array[x + 1 :]]
            right = array[x][y + 1 :]
            current_position = array[x][y]
            for n, quadrant in enumerate([up, left, down, right]):
                # print(y-1, x-1)
                current_bool = [current_position > element for element in quadrant]
                # print(n)
                scenic_scores[y - 1][x - 1][n] = current_bool
    return scenic_scores

def height_score(entry: list) -> int:
    '''Happy Linter'''
    scores = []
    for x in entry:
        try:
            score = x.index(False) + 1
            scores.append(score)
        except ValueError:
            score = sum(x)
            scores.append(score)
    return prod(scores)

def get_max_score(scores):
    '''Happy Linter'''
    tally = []
    for x in range(len(scores)):
        tally.extend(height_score(scores[y][x]) for y in range(len(scores)))
    return max(tally)

def solution():
    '''Happy Linter'''
    input_of_problem = open_input()
    print(part_one(input_of_problem))
    print(get_max_score(part_two(input_of_problem)))

solution()
