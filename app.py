import curses
from console_ui import handle_keypress, display_output, clear_ui
from controler import get_random_puzzle, get_empty_cell
from models import get_sorted_puzzle


def main():
    """Fonction principale de l'application"""
    try:
        # Récupération d'un taquin tiré aléatoirement
        # puzzle = get_sorted_puzzle()
        puzzle = get_random_puzzle()
        # get_empty_cell(puzzle)

        while True:
            # Attend une action et affiche le résultat
            puzzle = handle_keypress(puzzle)
            display_output(puzzle)

            # Frequence de rafraichissement
            curses.napms(50)  # ms
    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        clear_ui()


if __name__ == "__main__":
    main()
