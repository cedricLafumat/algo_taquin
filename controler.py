from models import get_sorted_puzzle, is_correct, randomize_puzzle, make_movement, get_empty_cell
from settings import PUZZLE_SIZE


def get_available_movements(puzzle):
    # TODO : retourner une liste de mouvements possibles ["LEFT", "UP"]
    x,y = get_empty_cell(puzzle)
    movements = ["UP","DOWN","LEFT","RIGHT"]
    if x == 0:
        movements.remove("UP")
    if x == PUZZLE_SIZE-1:
        movements.remove("DOWN")
    if y == 0:
        movements.remove("LEFT")
    if y == PUZZLE_SIZE-1:
        movements.remove("RIGHT")
    return movements


def move(movement, puzzle):
    # TODO :
    # * récupérer les mouvements possibles pour l'état en cours
    # * appliquer le mouvement si c'est permis
    # * retourner l'état modifié
    if movement in get_available_movements(puzzle):
        puzzle = make_movement(movement, puzzle)
    return puzzle


def get_correct_puzzle():
    puzzle = get_sorted_puzzle()
    return puzzle


def has_won(puzzle):
    puzzle = is_correct(puzzle)
    return puzzle


def get_random_puzzle():
    puzzle = get_sorted_puzzle()
    puzzle = randomize_puzzle(puzzle)
    return puzzle


# if __name__ == "__main__":
#     puzzle = get_sorted_puzzle()

