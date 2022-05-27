##############################################################################
# FILE: game.py
# WRITER: Ziv Fox
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: implementation of class Board following the API of ex9.
##############################################################################

class Board:
    """
    implementation of class Board following the API of ex9.
    """
    __EMPTY_CELL = '_'
    __EXIT = 'E'
    __BORDER = '*'
    __ROWS = 7
    __COLS = 7
    __EXIT_INDEX = (3, 7)

    def __create_empty_board(self):
        """:return: an empty board"""
        empty_board = []
        for row in range(Board.__ROWS):
            empty_board.append([Board.__EMPTY_CELL] * Board.__COLS
                               + [Board.__BORDER])
        empty_board[Board.__EXIT_INDEX[0]][Board.__EXIT_INDEX[1]] \
            = Board.__EXIT
        return empty_board

    def __init__(self):
        """object type Board constructor"""
        self.__board = self.__create_empty_board()
        self.__cars_dct = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        to_print = []
        for row in self.__board:
            to_print.append(' '.join(row))
        return '\n'.join(to_print)

    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_list = [self.target_location()]
        for row in range(Board.__ROWS):
            for col in range(Board.__COLS):
                cell_list.append((row, col))
        return cell_list

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name, movekey, description)
                 representing legal moves
        """
        moves_lst = []
        for c in self.__cars_dct.values():  # for each car on the board
            for move in c.possible_moves().items():  # for each move of the car
                for cell in c.movement_requirements(move[0]):
                    if not self.__is_legal_cell(cell):
                        break
                else:
                    moves_lst.append((c.get_name(), move[0], move[1]))
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return Board.__EXIT_INDEX

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if self.__board[coordinate[0]][coordinate[1]] not in \
                (Board.__EMPTY_CELL, Board.__EXIT):
            return self.__board[coordinate[0]][coordinate[1]]

    def __is_legal_cell(self, cell):
        """:return: True if cell is empty & within board, else False"""
        if cell not in self.cell_list() or \
                self.cell_content(cell) is not None:
            return False
        return True

    def add_car(self, car):
        """
        Adds a car to the game
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if car.get_name() in self.__cars_dct.keys():  # is same name?
            return False
        for cell in car.car_coordinates():  # are all cells legal?
            if not self.__is_legal_cell(cell):
                return False
        for cell in car.car_coordinates():
            self.__board[cell[0]][cell[1]] = car.get_name()
        self.__cars_dct[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for move in self.possible_moves():
            if (name, movekey) == (move[0], move[1]):  # if move is legal
                old_cells = self.__cars_dct[name].car_coordinates()
                if self.__cars_dct[name].move(movekey):  # if car supports move
                    for cell in old_cells:  # clear old location
                        self.__board[cell[0]][cell[1]] = self.__EMPTY_CELL
                    for cell in self.__cars_dct[name].car_coordinates():
                        self.__board[cell[0]][cell[1]] = name
                    return True
        return False
