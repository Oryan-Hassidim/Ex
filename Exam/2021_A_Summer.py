
from dataclasses import dataclass
from typing import Any


@dataclass
class Tree:
    data: int
    left: Any
    right: Any
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left, self.right = left, right


def is_leaf(tree):
    return tree.right is None and tree.left is None


def closest(val, x, y):
    if val == x or val == y:
        return val
    if abs(x-val) < abs(y-val):
        return x
    return y


def closest_value(tree: Tree, val: int):
    if tree.data == val or is_leaf(tree):
        return tree.data

    t = tree.left if tree.data > val else tree.right
    if t is None: return tree.data

    return closest(val, tree.data,
                   closest_value(t, val))


tree = Tree(9,
            Tree(5,
                 Tree(2),
                 Tree(7)),
            Tree(26,
                 None,
                 Tree(30,
                      None,
                      Tree(100))))

closest_value(tree, 1) #2
closest_value(tree, 2) #2
closest_value(tree, 8) #7 or 9
closest_value(tree, 29) #30
closest_value(tree, 80) #100
closest_value(tree, 105) #100

