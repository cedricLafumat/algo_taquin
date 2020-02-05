import random
from settings import EMPTY_CELL_VALUE, PUZZLE_SIZE


def get_empty_cell(puzzle):
    for x, row in enumerate(puzzle):
        for y, cell in enumerate(row):
            if cell == EMPTY_CELL_VALUE:
                return x,y


def get_sorted_puzzle():
    # Taquin correct, dans l'ordre
    correct_solution = [list(a) for a in
                        zip(*[iter(list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE])] * PUZZLE_SIZE)]
    return correct_solution


def is_correct(puzzle):
    # TODO : vérifier si le jeu est gagné
    pass


def randomize_puzzle(puzzle):
    # TODO : certains états random ne sont pas solvables,
    # il faut que cette fonction ne renvoie que des états solvables
    cases = list(range(1, PUZZLE_SIZE ** 2)) + [EMPTY_CELL_VALUE]
    random.shuffle(cases)
    return [list(a) for a in zip(*[iter(cases)] * PUZZLE_SIZE)]


def make_movement(movement, puzzle):
    x, y = get_empty_cell(puzzle)
    x2,y2 = x,y
    if movement == "UP":
        x2 = x - 1
    if movement == "DOWN":
        x2 = x + 1
    if movement == "RIGHT":
        y2 = y + 1
    if movement == "LEFT":
        y2 = y - 1
    puzzle[x][y] = puzzle[x2][y2]
    puzzle[x2][y2] = EMPTY_CELL_VALUE
    return puzzle
