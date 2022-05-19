####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 15/05/2022  23:45
####################################################################


from random import randint, choice
import sys
import traceback


def logit(file_name):
    from random import choice
    options = [False]*20+[True]+[False]*20
    def log(func):
        def wrapper(*args, **kwargs):
            if choice(options):
                with open(file_name, "a") as f:
                    result = func(*args, **kwargs)
                    line = f"assert {func.__name__}({','.join(map(repr, args))}) == {result}\n"
                    f.write(line)
                    return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return log


def run_test(name, func):
    try:
        func()
        print(f"\033[1;32m{name} test PASSED")
        print("\033[0m", end="")
        return 1
    except Exception as e:
        print(f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}")
        print(traceback.format_exc())
    print("\033[0m", end="")
    return 0


def main():
    tests = [
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

