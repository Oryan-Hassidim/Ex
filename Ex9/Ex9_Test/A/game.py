##############################################################################
# FILE: game.py
# WRITER: Ziv Fox
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: implementation of class Game following the API of ex9.
##############################################################################

import sys
import helper
import board
import car


class Game:
    """
    implementation of class Game following the API of ex9.
    """

    __CARS_NAMES = ['Y', 'B', 'O', 'G', 'W', 'R']

    def __init__(self, board):
        """
        Initialize a new Game object
        :param board: An object of type board
        """
        self.__board = board

    def __is_legal_input(self, users_input):
        """
        :return: True if users_input is legal, else False
        """
        if len(users_input) != 3 or users_input[1] != ',' \
                or users_input[2] not in ['u', 'd', 'r', 'l'] \
                or users_input[0] not in self.__CARS_NAMES:
            return False
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.__board)
        while self.__board.cell_content(self.__board.target_location()) \
                is None:  # while not win
            users_input = input("please enter car,move")
            if users_input == '!':  # exit play
                break
            if not self.__is_legal_input(users_input) or \
                    not self.__board.move_car(users_input[0], users_input[2]):
                print("illegal input!")
                continue
            else:
                print(self.__board)


if __name__ == "__main__":
    board1 = board.Board()
    for c in helper.load_json(sys.argv[1]).items():
        name, length, location, orientation = c[0], c[1][0], c[1][1], c[1][2]
        if name in ['Y', 'B', 'O', 'G', 'W', 'R'] and length in [2, 3, 4] and \
                orientation in [0, 1]:
            board1.add_car(car.Car(name, length, location, orientation))
    Game(board1).play()
