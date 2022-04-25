from ex7 import mult, is_even, log_mult, is_power, compare_2d_lists
from random import randint, random


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
        assert not is_power(randint(1,1000), 0)
        assert is_power(randint(1,1000), 1)
    for _ in range(100):
        b = randint(2, 100)
        x1 = b ** randint(1, 15)
        x2 = b
        while x2 % b == 0 or x2 == 1:
            x2 = b * (randint(0,1) + random())
            x2 = round(x2)
        x2 = x2 ** randint(1, 15)
        assert is_power(b, x1)
        assert not is_power(b, x2)

def test_compare_2d_lists():
    assert compare_2d_lists([],[])
    assert not compare_2d_lists([],[[]])
    assert compare_2d_lists([[]],[[]])
    assert not compare_2d_lists([[1]],[[]])
    assert compare_2d_lists([[1]],[[1]])
    assert not compare_2d_lists([[],[]],[[]])
    assert not compare_2d_lists([[],[]],[[1]])
    assert compare_2d_lists([[],[]],[[],[]])
    assert compare_2d_lists([[1],[]],[[1],[]])
    assert not compare_2d_lists([[1],[]],[[2],[]])
    assert compare_2d_lists([[1],[2,3]],[[1],[2,3]])


        
        