####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 02/05/2022  22:40
####################################################################


from random import randint, random, choice
import sys
import subprocess
from typing import Set

from puzzle_solver import max_seen_cells, min_seen_cells, check_constraints, solve_puzzle, how_many_solutions


def test_max_seen_cells():
    picture = [[-1, 0, 1, -1],
               [0, 1, -1, 1],
               [1, 0, 1, 0]]
    assert max_seen_cells(picture, 0, 0) == 1
    assert max_seen_cells(picture, 1, 0) == 0
    assert max_seen_cells(picture, 1, 2) == 5
    assert max_seen_cells(picture, 1, 1) == 3


def test_min_seen_cells():
    picture = [[-1, 0, 1, -1],
               [0, 1, -1, 1],
               [1, 0, 1, 0]]
    assert min_seen_cells(picture, 0, 0) == 0
    assert min_seen_cells(picture, 1, 0) == 0
    assert min_seen_cells(picture, 1, 2) == 0
    assert min_seen_cells(picture, 1, 1) == 1


def test_check_constraints():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [
        [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == None
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) in [
        [[0, 0, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]


def test_how_many_solutions():
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == 1
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == 0
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3)
                              for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64
