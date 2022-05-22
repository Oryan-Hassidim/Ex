####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 22/05/2022  03:18
####################################################################


from random import randint, choice
import sys
from sys import executable
from os import mkdir, rmdir
from os.path import join, isdir, isfile
import traceback
from subprocess import PIPE, run
from shutil import copyfile, rmtree


def combination_test(car_folder, board_folder, game_folder, *tests_files):
    if isdir("TESTS"):
        rmtree("TESTS")
    mkdir("TESTS")
    copyfile("helper.py", join("TESTS", "helper.py"))
    try:
        copyfile(join(car_folder, "car.py"), join("TESTS", "car.py"))
        copyfile(join(board_folder, "board.py"), join("TESTS", "board.py"))
        copyfile(join(game_folder, "game.py"), join("TESTS", "game.py"))
    except FileNotFoundError:
        rmtree("TESTS")
        return
    for test_file in tests_files:
        copyfile("_"+test_file, join("TESTS", test_file))
    out = run([executable, "-m", "pytest",  "TESTS"], shell=True)
    if out.returncode != 0:
        raise Exception("pytest failed")


def test_A():
    combination_test("A", "A", "A", "test_car.py",
                     "test_board.py", "test_game.py")


def test_B():
    combination_test("B", "B", "B", "test_car.py",
                     "test_board.py", "test_game.py")


def test_C():
    combination_test("C", "C", "C", "test_car.py",
                     "test_board.py", "test_game.py")


def W_test(A_or_B_or_C):
    combination_test("W", A_or_B_or_C, A_or_B_or_C,
                     "test_wcar_board.py", "test_wcar_game.py")
    combination_test(A_or_B_or_C, "W", A_or_B_or_C,
                     "test_wboard_game.py")
    combination_test("W", "W", A_or_B_or_C,
                     "test_wcar_wboard_game.py")


def test_WA():
    W_test("A")


def test_WB():
    W_test("B")


def test_WC():
    W_test("C")


def test_combinations():
    for car in "ABC":
        for board in "ABC":
            for game in "ABC":
                if car == board and car == game:
                    continue
                try:
                    combination_test(car, board, game,
                                     "test_car.py",
                                     "test_board.py",
                                     "test_game.py")
                    print(
                        f"\033[1;32mcar: {car}, board: {board}, game: {game} PASSED\033[0m")
                except Exception:
                    print(
                        f"\033[1;31mcar: {car}, board: {board}, game: {game} FAILED\033[0m")


def run_test(name, func):
    try:
        func()
        print(f"\033[1;32m{name} test PASSED\033[0m")
        return 1
    except Exception as e:
        print(
            f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}\033[0m")
        print(traceback.format_exc())
    print("\033[0m", end="")
    return 0


def main():
    tests = [
        "A",
        "B",
        "C",
        "WA",
        "WB",
        "WC",
        "combinations"
    ]
    count = 0
    for test in tests:
        count += run_test(test, globals()["test_" + test])
    print()
    if count == len(tests):
        print("\033[1;32m==============All OK==============")
    else:
        print(f"\033[1;31m========={count}/{len(tests)} tests passed=========")
    print("\033[0m")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
