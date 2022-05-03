
#################################################################################
# FILE: puzzle_solver.py
# WRITER: Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE: Intro2cs2 ex8 2021-2022
# DESCRIPTION: app for finding solutions for the puzzle
# NOTES:
#################################################################################

from subprocess import check_call
from typing import List, Tuple, Set, Optional, Generator


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]

B = 0  # black
W = 1  # white
U = -1  # unknown


def check_bounds(matrix, i, j):
    """
    Checks if the given index is in the bounds of the matrix.
    :param matrix: a matrix
    :param i: the row index
    :param j: the column index
    """
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def seen_cells(picture: Picture, row: int, col: int, blocks_values: Set[int]) -> int:
    """
    Returns the number of cells that are seen by a white cell in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    :param blocks_values: blocks values
    """
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if picture[row][col] in blocks_values:
        return 0
    seen_cells = 1
    for di, dj in directions:
        i, j = row + di, col + dj
        while check_bounds(picture, i, j) and picture[i][j] not in blocks_values:
            seen_cells += 1
            i, j = i + di, j + dj
    return seen_cells


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the maximum number of cells that can be seen by a white cell
    in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    """
    return seen_cells(picture, row, col, {B})


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the maximum number of cells that can be seen by a white cell
    in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    """
    return seen_cells(picture, row, col, {B, U})


def check_constraint(picture: Picture, constraint: Constraint) -> int:
    """
    Checks if the given constraint is satisfied.
    :param picture: a picture
    :param constraint: a constraint
    :return: 1 if the constraint is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    i, j, seen = constraint
    min_seen = min_seen_cells(picture, i, j)
    max_seen = max_seen_cells(picture, i, j)
    if max_seen == min_seen == seen:
        return 1
    if min_seen <= seen <= max_seen:
        return 2
    return 0


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    Checks if the given picture satisfies all the constraints in the set.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :return: 1 if the constraints is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    res = set()
    for constraint in constraints_set:
        res.add(check_constraint(picture, constraint))
        if 0 in res:
            return 0
    if 2 in res:
        return 2
    return 1


def check_constraints_on_cell(picture, constraints_set, width, ij) -> int:
    """
    Checks if the given picture satisfies all the constraints in the set.
    Starts with the given cell.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :return: 1 if the constraints is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    if ij == -1:
        return check_constraints(picture, constraints_set)

    row, col = ij // width, ij % width
    constraints = {(i, j, seen)
                   for i, j, seen in constraints_set if i == row or j == col}
    check_val_c = check_constraints(picture, constraints)
    if check_val_c == 0:
        return 0
    rest = check_constraints(picture, constraints_set - constraints)
    return max(check_val_c, rest)


def fill(picture, constraints_set, size, width, ij=0):
    """
    Generates all the possible pictures that can be obtained by filling the given picture.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param size: the size of the picture
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :return: generator of solutions
    """
    if ij == size:
        assert check_constraints(picture, constraints_set)
        yield picture
        return

    i, j = ij // width, ij % width
    original = picture[i][j]
    for fill_option in ({W, B} if original == U else {original}):
        picture[i][j] = fill_option
        for sol in fill(picture, constraints_set, size, width, ij + 1):
            yield sol
    picture[i][j] = original


def find_solutions_core(picture, constraints_set, size, width, ij=0, check=True):
    """
    Finds all solutions to the puzzle using backtracking.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param size: the size of the picture
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :param check: True if checking for this cell is needed, else False
    :return: generator of solutions
    """
    if ij == size:
        if check_constraints(picture, constraints_set):
            yield picture
        return

    if check:
        check_val = check_constraints_on_cell(
            picture, constraints_set, width, ij - 1)
        if check_val == 0:
            return

        if check_val == 1:
            for sol in fill(picture, constraints_set, size, width, ij):
                yield sol
            return

    # check_val == 2
    i, j = ij // width, ij % width
    original = picture[i][j]
    for option in ({W, B} if original == U else {original}):
        picture[i][j] = option
        for sol in find_solutions_core(picture, constraints_set, size, width, ij + 1, option != original):
            yield sol
        picture[i][j] = original


def find_solutions(constraints_set: Set[Constraint], n: int, m: int) -> Generator[Picture, None, None]:
    """
    Finds all solutions to the puzzle using backtracking.
    :param constraints_set: a set of constraints
    :param n: the number of rows
    :param m: the number of columns
    :return: generator of solutions
    """
    picture = [[U] * m for _ in range(n)]
    for i, j, seen in constraints_set:
        if seen == 0:
            picture[i][j] = B
        else:
            picture[i][j] = W
    for sol in find_solutions_core(picture, constraints_set, n*m, m):
        yield sol


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    Solves the puzzle using backtracking.
    :param constraints_set: a set of constraints
    :param n: the number of rows
    :param m: the number of columns
    :return: the solution if it exists, else None
    """
    for sol in find_solutions(constraints_set, n, m):
        return sol
    return None


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    return len(list(find_solutions(constraints_set, n, m)))


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...


def sol_to_str(sol):
    s = chr(9607) * 2
    b = "\033[30m" + s
    w = "\033[37m" + s
    return "\n".join(["".join([b if c == B else w for c in row]) for row in sol])


def main():
    for sol in find_solutions({(0, 2, 3), (1, 1, 4)}, 3, 3):
        print(sol_to_str(sol), end="\033[0m\n\n")


if __name__ == "__main__":
    main()
