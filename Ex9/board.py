from typing import Tuple, List, Optional, Dict, Any

Coordinates = Tuple[int, int]
# Orientation = Literal[0, 1]
VERTICAL = 0
HORIZONTAL = 1
# Movekey = Literal['u', 'd', 'r', 'l']
ORIENTATIONS = {0: (1, 0), 1: (0, 1)}
DIRECTIONS = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (1, 0)}
MOVE_KEYS = ['u', 'd', 'r', 'l']
EMPTY_STR = "- "
COLORS = {
    'Y': "\033[43;30mY \033[0m",
    'B': "\033[44;37mB \033[0m",
    'O': "\033[46;30mO \033[0m",
    'W': "\033[47;30mB \033[0m",
    'G': "\033[42;30mG \033[0m",
    'R': "\033[41;30mR \033[0m"
}


class Board:
    """
    Game object of single board for rush-hour game.
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        board = {}
        for i in range(4):
            for j in range(7):
                board[i, j] = None
        board[3, 7] = None
        for i in range(4, 7):
            for j in range(7):
                board[i, j] = None
        self.__board = board
        self.__cars: List[Any] = []

    def __format_cell(self, i, j):
        """
        Return the formatted string representation of the cell at coordinates (i, j).
        """
        cell = self.__board[i, j]
        if cell is None:
            return "**" if (i, j) == self.target_location() else EMPTY_STR
        else:
            if cell.get_name() in COLORS:
                return COLORS[cell.get_name()]
            return cell.get_name()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        res = ""
        board = self.__board
        res += "\n".join("".join(self.__format_cell(i, j)
                                 for j in range(7))
                         for i in range(4))
        res += (self.__format_cell(3, 7)) + "\n"
        res += "\n".join("".join(self.__format_cell(i, j)
                                 for j in range(7))
                         for i in range(4, 7))
        return res

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        return list(self.__board.keys())

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name, movekey, description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        board = self.__board
        return [(car.get_name(), movkey, description)
                for car in self.__cars
                for movkey, description in car.possible_moves().items()
                if all((i, j) in board
                       and board[i, j] is None
                       for i, j in car.movement_requirements(movkey))]

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        i, j = coordinate
        return None if self.__board[i, j] is None else self.__board[i, j].get_name()

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        board = self.__board
        if car in self.__cars or car.get_name() in (car.get_name() for car in self.__cars):
            return False
        if not all((i, j) in board
                   and board[i, j] is None
                   for i, j in car.car_coordinates()):
            return False
        self.__cars.append(car)
        for i, j in car.car_coordinates():
            board[i, j] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if name not in (car.get_name() for car in self.__cars):
            return False
        car = next(car for car in self.__cars if car.get_name() == name)
        if movekey not in car.possible_moves():
            return False
        if not all((i, j) in self.__board
                   and self.__board[i, j] is None
                   for i, j in car.movement_requirements(movekey)):
            return False
        for i, j in car.car_coordinates():
            self.__board[i, j] = None
        car.move(movekey)
        for i, j in car.car_coordinates():
            self.__board[i, j] = car
        return True

    def __repr__(self):
        return f"Board({self.__board}, {self.__cars})"
