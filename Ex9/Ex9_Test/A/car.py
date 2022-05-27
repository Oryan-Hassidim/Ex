##############################################################################
# FILE: car.py
# WRITER: Ziv Fox
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: implementation of class Car following the API of ex9.
##############################################################################

class Car:
    """
    implementation of class Car following the API of ex9.
    """

    __VERTICAL = 0
    __HORIZONTAL = 1

    __UP = 'u'
    __DOWN = 'd'
    __RIGHT = 'r'
    __LEFT = 'l'

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length
        :param location: A tuple representing the car's head (row, col)
                         location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = []
        self.__location.append(location[0])
        self.__location.append(location[1])
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = []
        if self.__orientation == Car.__VERTICAL:
            for ind in range(self.__length):
                coordinates.append((self.__location[0] + ind,
                                    self.__location[1]))
        elif self.__orientation == Car.__HORIZONTAL:
            for ind in range(self.__length):
                coordinates.append((self.__location[0],
                                    self.__location[1] + ind))
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == Car.__VERTICAL:
            return {Car.__UP: "move one index upwards",
                    Car.__DOWN: "move one index downwards"}
        elif self.__orientation == Car.__HORIZONTAL:
            return {Car.__RIGHT: "move one index to the right",
                    Car.__LEFT: "move one index to the left"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this
        move to be legal.
        """
        if self.__orientation == Car.__VERTICAL:
            if movekey == Car.__UP:
                return [(self.__location[0] - 1, self.__location[1])]
            elif movekey == Car.__DOWN:
                return [(self.car_coordinates()[self.__length - 1][0] + 1,
                         self.car_coordinates()[self.__length - 1][1])]
        elif self.__orientation == Car.__HORIZONTAL:
            if movekey == Car.__RIGHT:
                return [(self.car_coordinates()[self.__length - 1][0],
                         self.car_coordinates()[self.__length - 1][1] + 1)]
            elif movekey == Car.__LEFT:
                return [(self.__location[0], self.__location[1] - 1)]
        return []

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__orientation == Car.__VERTICAL:
            if movekey == Car.__UP:
                self.__location[0] -= 1
                return True
            elif movekey == Car.__DOWN:
                self.__location[0] += 1
                return True
        elif self.__orientation == Car.__HORIZONTAL:
            if movekey == Car.__RIGHT:
                self.__location[1] += 1
                return True
            elif movekey == Car.__LEFT:
                self.__location[1] -= 1
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
