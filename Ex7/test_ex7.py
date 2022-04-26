from typing import Set
from ex7 import magic_list, mult, is_even, log_mult, is_power, compare_2d_lists, reverse, number_of_ones
from random import randint, random, choice
import sys
from itertools import tee
if sys.version_info.minor < 10:
    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
else:
    from itertools import pairwise


def generate_letter():
    return chr(randint(ord("A"), ord("z") + 1))


def generate_string(length):
    """Returns new string with different chars"""
    p = set(range(ord("A"), ord("z") + 1))
    s = ""
    for _ in range(length):
        c = chr(choice(list(p)))
        p -= {c}
        s += c
    return s


def test_mult():
    for _ in range(100):
        x = randint(0, 100) + random()
        y = randint(0, 100)
        assert abs(mult(x, y) - x * y) < 0.01


def test_is_even():
    for x in range(100):
        x = randint(0, 100)
        assert is_even(x) == (x % 2 == 0)


def test_log_mult():
    for _ in range(100):
        x = randint(0, 100) + random()
        y = randint(0, 100)
        assert abs(log_mult(x, y) - x * y) < 0.01


def test_is_power():
    assert is_power(0, 0)
    for x in range(20):
        assert not is_power(randint(1, 1000), 0)
        assert is_power(randint(1, 1000), 1)
    for _ in range(100):
        b = randint(2, 100)
        x1 = b ** randint(1, 15)
        x2 = b
        while x2 % b == 0 or x2 == 1:
            x2 = b * (randint(0, 1) + random())
            x2 = round(x2)
        x2 = x2 ** randint(1, 15)
        assert is_power(b, x1)
        assert not is_power(b, x2)


def test_reverse():
    assert reverse('') == ''
    assert reverse('a') == 'a'
    assert reverse('ab') == 'ba'
    for _ in range(100):
        str = generate_string(randint(1, 100))
        assert reverse(str) == str[::-1]


def test_number_of_ones():
    assert number_of_ones(0) == 0
    assert number_of_ones(1) == 1
    assert number_of_ones(10) == 2
    assert number_of_ones(100) == 21
    assert number_of_ones(200) == 20 + 20 + 100


def test_compare_2d_lists():
    assert compare_2d_lists([], [])
    assert not compare_2d_lists([], [[]])
    assert compare_2d_lists([[]], [[]])
    assert not compare_2d_lists([[1]], [[]])
    assert compare_2d_lists([[1]], [[1]])
    assert not compare_2d_lists([[], []], [[]])
    assert not compare_2d_lists([[], []], [[1]])
    assert compare_2d_lists([[], []], [[], []])
    assert compare_2d_lists([[1], []], [[1], []])
    assert not compare_2d_lists([[1], []], [[2], []])
    assert compare_2d_lists([[1], [2, 3]], [[1], [2, 3]])


def collect_deep(iterable, ids: Set[int]):
    for x in iterable:
        assert id(x) not in ids
        ids.add(id(x))
        if isinstance(x, list):
            collect_deep(x, ids)


def test_magic_list():
    ids = set()
    lst = list(map(magic_list, range(10)))
    collect_deep(lst, ids)
    for a, b in pairwise(lst):
        assert b[-1] == a
