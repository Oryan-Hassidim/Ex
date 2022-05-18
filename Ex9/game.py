
from typing import Tuple, Literal, List, Optional, Dict
from sys import argv, exit
from helper import load_json
from os.path import isfile

from car import Car
from board import Board

Coordinates = Tuple[int, int]
Orientation = Literal[0, 1]
VERTICAL = 0
HORIZONTAL = 1
Movekey = Literal['u', 'd', 'r', 'l']
ORIENTATIONS = {0: (1, 0), 1: (0, 1)}
DIRECTIONS = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (1, 0)}
MOVE_KEYS = ['u', 'd', 'r', 'l']
SUPPORTED_LENGTHS = {2, 3, 4}
SUPPORTED_NAMES = {'Y', 'B', 'O', 'W', 'G', 'R'}

WELCOME_MESSAGE = "Welcome to Rush-Hour!"
WIN_MESSAGE = """You won!

WIN     WIN     WIN    WIN    WIN     WIN
 WIN   WIWIN   WIN     WIN    WININ   WIN
  WIN WIN WIN WIN      WIN    WIN WIN WIN
   WININ   WININ       WIN    WIN   WIWIN
    WIN     WIN        WIN    WIN     WIN
"""
LOSE_MESSAGE = "You lost! :("


class Game:
    """
    Game object for managing single game.
    """

    def __init__(self, board: Board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board

    def __print_error(self):
        print("Invalid command!")
        print("Valid commands are: ")
        for color, direction, description in self.__board.possible_moves():
            print(f"{color},{direction}  --  {description}")
        print("\nCurrent state:")
        print(self.__board, end="\n\n")

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
               direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        command = input("Enter command: ")
        if command == "!":
            return False
        if len(command) != 3 or command[1] != ',':
            self.__print_error()
            return True

        color = command[0]
        movekey = command[2]
        board = self.__board
        if (color, movekey) not in ((c, d) for c, d, _ in board.possible_moves()):
            self.__print_error()
            return True
        if board.move_car(color, movekey):
            print(board, end="\n\n")
        else:
            self.__print_error()
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        print(WELCOME_MESSAGE)
        print("Your board:")
        board = self.__board
        print(board)
        while self.__single_turn() and board.cell_content(board.target_location()) is None:
            pass
        if board.cell_content(board.target_location()) is not None:  # win
            print(WIN_MESSAGE)
        else:
            print(LOSE_MESSAGE)


def initialize_board(json):
    board = Board()
    for name, (length, (i, j), orientation) in json.items():
        if name not in SUPPORTED_NAMES:
            print(
                f"the name {name} is not supported! {SUPPORTED_NAMES} only allowed!")
            return
        if length not in SUPPORTED_LENGTHS:
            print(
                f"the length {length} is not supported! {SUPPORTED_LENGTHS} only allowed")
            return
        if (i, j) not in board.cell_list():
            print(f"the coordinates {(i,j)} is not supported!")
            return
        if orientation not in ORIENTATIONS:
            print(f"the orientation {orientation} is not supported!\
                    {ORIENTATIONS.keys()} only allowed!")
            return
        try:
            car = Car(name, length, (i, j), orientation)
        except Exception as e:
            print(e)
            return

        if not board.add_car(car):
            print(f"unexpected error wit car {name}.")
            return
    return board


def main(args):
    if len(args) < 1:
        print("one argument of config file needed!")
        return
    if not isfile(args[0]):
        print(f"there is not file in path: {args[0]}")
        return
    board = initialize_board(load_json(args[0]))
    if board is None:
        return 1
    game = Game(board)
    game.play()


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    # exit(int(main(argv[1:]) or 0))
    main(argv[1:])
