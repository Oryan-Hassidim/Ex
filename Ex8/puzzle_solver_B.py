###########################################################################
# FILE: puzzle_solve.py
# WRITERS: Bezalel Yanir 208814616
# EXERCISE: Intro2cs2 ex8 2021-2022
# DESCRIPTION: solves black and solve
###########################################################################


from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint
# (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


# def max_seen_cells(picture: Picture, row: int, col: int) -> int:
#    """
#    return number of white cells next to the row,co, cell. consider
#    undifined cells as white/
#    """
#    if picture[row][col] == 0:
#        return 0
#    return (right_helper(picture, row, col, 'MAX') +
#            left_helper(picture, row, col, 'MAX') +
#            up_helper(picture, row, col, 'MAX') +
#            down_helper(picture, row, col, 'MAX') + 1)

B = 0  # black
W = 1  # white
U = -1  # unknown


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == B:
        return 0
    count = 1
    i, j = row - 1, col - 1
    while i >= 0 and picture[i][col] != B:
        count, i = count + 1, i - 1
    while j >= 0 and picture[row][j] != B:
        count, j = count + 1, j - 1
    i, j = row + 1, col + 1
    while i < len(picture) and picture[i][col] != B:
        count, i = count + 1, i + 1
    while j < len(picture[0]) and picture[row][j] != B:
        count, j = count + 1, j + 1
    return count


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] != W:
        return 0
    count = 1
    i, j = row - 1, col - 1
    while i >= 0 and picture[i][col] == W:
        count, i = count + 1, i - 1
    while j >= 0 and picture[row][j] == W:
        count, j = count + 1, j - 1
    i, j = row + 1, col + 1
    while i < len(picture) and picture[i][col] == W:
        count, i = count + 1, i + 1
    while j < len(picture[0]) and picture[row][j] == W:
        count, j = count + 1, j + 1
    return count


def right_helper(picture, row, col, min_max, i=0):
    """
    return number of white cells next to the row,co, cell from right
    """
    if col >= len(picture[0]):
        return 0
    if min_max == 'MAX':
        if picture[row][col] != 0:
            return i + right_helper(picture, row, col + 1, min_max, 1)
    if min_max == 'MIN':
        if picture[row][col] == 1:
            return i + right_helper(picture, row, col + 1, min_max, 1)
    return 0


def left_helper(picture, row, col, min_max, i=0):
    """
    return number of white cells next to the row,co, cell from left
    """
    if col < 0:
        return 0
    if min_max == 'MAX':
        if picture[row][col] != 0:
            return i + left_helper(picture, row, col - 1, min_max, 1)
    if min_max == 'MIN':
        if picture[row][col] == 1:
            return i + left_helper(picture, row, col - 1, min_max, 1)
    return 0


def up_helper(picture, row, col, min_max, i=0):
    """
    return number of white cells next to the row,co, cell from up
    """
    if row < 0:
        return 0
    if min_max == 'MAX':
        if picture[row][col] != 0:
            return i + up_helper(picture, row - 1, col, min_max, 1)
    if min_max == 'MIN':
        if picture[row][col] == 1:
            return i + up_helper(picture, row - 1, col, min_max, 1)
    return 0


def down_helper(picture, row, col, min_max, i=0):
    """
    return number of white cells next to the row,co, cell from down
    """
    if row >= len(picture):
        return 0
    if min_max == 'MAX':
        if picture[row][col] != 0:
            return i + down_helper(picture, row + 1, col, min_max, 1)
    if min_max == 'MIN':
        if picture[row][col] == 1:
            return i + down_helper(picture, row + 1, col, min_max, 1)
    return 0


# def min_seen_cells(picture: Picture, row: int, col: int) -> int:
#    """
#    return number of white cells next to the row,co, cell. consider
#    undifined cells as black.
#    """
#    if picture[row][col] != 1:
#        return 0
#    return (right_helper(picture, row, col, 'MIN') +
#            left_helper(picture, row, col, 'MIN') +
#            up_helper(picture, row, col, 'MIN') +
#            down_helper(picture, row, col, 'MIN') + 1)


def check_constraints(picture: Picture,
                      constraints_set: Set[Constraint]) -> int:
    """
    check if picture match all constraints
    """
    for constrain in constraints_set:
        x = _check_single(picture, constrain)
        if x == 0:
            return 0
        if x == 2:
            return 2
    return 1


def _check_single(picture, constrain):
    """
    check if picture match single constraint
    """
    mini = min_seen_cells(picture, constrain[0], constrain[1])
    maxi = max_seen_cells(picture, constrain[0], constrain[1])
    if mini == maxi == constrain[2]:
        return 1
    if mini <= constrain[2] <= maxi:
        return 2
    return 0


def solve_puzzle(constraints_set: Set[Constraint], n: int,
                 m: int) -> Optional[Picture]:
    """
    returns one solution for the puzzle
    """
    image = [[-1 for j in range(m)] for i in range(n)]
    solution = [[-1 for j in range(m)] for i in range(n)]
    for constrain in constraints_set:
        if constrain[2] == 0:
            image[constrain[0]][constrain[1]] = 0
        else:
            image[constrain[0]][constrain[1]] = 1
    solve_helper(constraints_set, image, 0, 0, solution, True)
    if is_solve(solution):
        return solution
    return


def is_solve(solution):
    """
    checks if "solution" really is solution
    """
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            if solution[i][j] == -1:
                return False
    return True


def solve_helper(const, picture, i, j, solution=[], sol=False):
    """
    helps solve_helper, how many solutions
    """
    check = check_constraints(picture, const)
    if check == 0:
        return 0
    if i == len(picture):
        if sol == True:
            solution = check_is_1(picture, solution)
        return 1
    if j == len(picture[0]):
        return solve_helper(const, picture, i+1, 0, solution, sol)
    if picture[i][j] == -1:
        picture[i][j] = 0
        black_solve = solve_helper(const, picture, i, j+1, solution, sol)
        picture[i][j] = 1
        white_solve = solve_helper(const, picture, i, j+1, solution, sol)
        picture[i][j] = -1
        return black_solve + white_solve
    else:
        return solve_helper(const, picture, i, j+1, solution, sol)


def check_is_1(picture, solution):
    """
    generates solution
    """
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            solution[i][j] = picture[i][j] + 0
    return solution


def how_many_solutions(constraints_set: Set[Constraint],
                       n: int, m: int) -> int:
    """
    return number of optional solutions
    """
    image = [[-1 for j in range(m)] for i in range(n)]
    for constrain in constraints_set:
        if constrain[2] == 0:
            image[constrain[0]][constrain[1]] = 0
        else:
            image[constrain[0]][constrain[1]] = 1
    solve = solve_helper(constraints_set, image, 0, 0)
    return solve


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """
    get picture, returns optional set of constraints
    """
    constrains = set()
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            amount = max_seen_cells(picture, i, j)
            constrains.add((i, j, amount))
    return generate_helper(picture, constrains)


def generate_helper(picture, constrains):
    """
    helps generate puzzle
    """
    if how_many_solutions(constrains, len(picture), len(picture[0])) > 1:
        return False  # true means last constrain removed can't be removed
    result = False
    for const in constrains:
        constrains.remove(const)
        result = result or generate_helper(picture, constrains)
        if isinstance(result, set):
            return result
        constrains.add(const)
    if result:
        return False
    return constrains


puzzle = {(4, 2, 1), (0, 0, 1), (2, 4, 5), (3, 0, 0), (5, 1, 2), (5, 6, 1), (4, 0, 3), (4, 4, 3),
          (6, 2, 2), (2, 0, 0), (1, 5, 2), (0, 3, 7), (6, 5, 0), (1, 2, 3), (3, 1, 0), (3, 6, 2), (5, 3, 0)}
print(solve_puzzle(puzzle, 7, 7))
