from random import randint
from time import sleep


# Q6
def thresholdgen(threshold: int):
    while True:
        sleep(0.1)
        n = randint(-100, 100)
        yield n, n >= threshold


class Learn:
    def __init__(self, gen):
        self.gen = gen
        self.min, self.max = None, None

    def evaluate(self, n):
        while True:
            if self.min is not None and n <= self.min:
                return False
            if self.max is not None and self.max <= n:
                return True

            num, t = next(self.gen)
            if t:
                self.max = min(self.max, num) if self.max is not None else num
            else:
                self.min = max(self.min, num) if self.min is not None else num

    def find_threshold(self):
        temp = 0
        while self.min is None:
            self.evaluate(temp)
            temp -= 100
        temp = 0
        while self.max is None:
            temp += 100
            self.evaluate(temp)

        while self.max - self.min > 1:
            temp = self.min + self.max
            self.evaluate(temp // 2)

        return self.max

    def __str__(self):
        return f"({self.min} {self.max})"

    def __repr__(self):
        return str(self)


gen = thresholdgen(7)
my_learner = Learn(gen)
my_learner.find_threshold()  # 7

my_learner.evaluate(8)  # True
my_learner.evaluate(7)  # True
my_learner.evaluate(6)  # False


# Q5
def fixed_point(f):
    def inner(x):
        last = f(x)
        while True:
            res = f(last)
            if res == last:
                return last
            last = res
    return inner


def f(x): return (x-2)*(x-2)


fp = fixed_point(f)

print(fp(2))
