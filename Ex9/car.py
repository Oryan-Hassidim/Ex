from typing import Tuple, Literal, Dict

Coordinates = Tuple[int, int]
Orientation = Literal[0, 1]
VERTICAL = 0
HORIZONTAL = 1
Movekey = Literal['u', 'd', 'r', 'l']
ORIENTATIONS = {0: (1, 0), 1: (0, 1)}
DIRECTIONS = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
MOVE_KEYS = ['u', 'd', 'r', 'l']
SUPPORTED_LENGTHS = {2, 3, 4}


class Car:
    """
    Game object of single car on the board.
    """
    def __add_coordinates(coor1, coor2):
        """
        :param coor1: A tuple of coordinates.
        :param coor2: A tuple of coordinates.
        :return: A tuple of coordinates representing the sum of the two input coordinates.
        """
        return (coor1[0] + coor2[0], coor1[1] + coor2[1])

    def __init__(self, name: str, length: int, location: Coordinates, orientation: Orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        if any(x < 0 for x in location):
            raise ValueError("location must be positive")
        if length not in SUPPORTED_LENGTHS:
            raise ValueError("length must be positive")
        if orientation not in ORIENTATIONS:
            raise ValueError("orientation must be 0 or 1")
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        d1, dj = ORIENTATIONS[self.__orientation]
        return [Car.__add_coordinates(self.__location, (d*d1, d*dj)) for d in range(self.__length)]

    def possible_moves(self) -> Dict[Movekey, str]:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        res = {}
        ori = self.__orientation
        if ori == VERTICAL:
            res['d'] = "cause the car to move one step down"
            if self.__location[0] > 0:
                res['u'] = "cause the car to move one step up"
        else:
            res['r'] = "cause the car to move one step right"
            if self.__location[1] > 0:
                res['l'] = "cause the car to move one step left"
        return res

    __first_or_last = {'u': 0, 'd': -1, 'l': 0, 'r': -1}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        if movekey not in self.possible_moves():
            raise ValueError("movekey must be one of possible movekeys")
        last_coor = self.car_coordinates()[Car.__first_or_last[movekey]]
        return [Car.__add_coordinates(last_coor, DIRECTIONS[movekey])]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if movekey not in MOVE_KEYS:
            raise ValueError("movekey must be one of 'udrl'")
        if movekey not in self.possible_moves():
            return False
        self.__location = Car.__add_coordinates(
            self.__location, DIRECTIONS[movekey])
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

    def __repr__(self):
        return f"Car({self.__name}, {self.__length}, {self.__location}, {self.__orientation})"
