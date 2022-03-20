#############################################################
# FILE : ex3.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex3 2022
# DESCRIPTION: Functions who used loops and lists.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES:
#############################################################


from functools import reduce
from typing import ForwardRef


def input_list():
    """The function get from the user list of numbers and returns
    list of the numbers and their sum."""
    lst = []
    lst_sum = 0
    current = input()
    while current != "":
        num = float(current)
        lst.append(num)
        lst_sum += num
        current = input()
    lst.append(lst_sum)
    return lst


def inner_product(vec_1, vec_2):
    """Function which gets two vectors as parameters and returns
    the value of their inner production.
    If the lengths of the functions is different, returns None."""
    count = len(vec_1)
    result = 0
    if count != len(vec_2):
        return None

    # We shouldn't use zip function, so we iterate by index.
    for i in range(count):
        result += vec_1[i] * vec_2[i]
    return result


def sequence_monotonicity(sequence):
    """Function which gets a list of numbers as parameter
    and returns a list with 4 elements:
        - result[0] := the sequence is monotonically increasing;
        - result[1] := the sequence is strictly increasing;
        - result[2] := the sequence is monotonically decreasing;
        - result[3] := the sequence is strictly decreasing"""

    # "No matter how large the list is, index lookup and assignment
    # take a constant amount of time and are thus O(1)."
    # https://bradfieldcs.com/algos/analysis/performance-of-python-types/
    # less CPU and time performance than 4 local variables,
    # but more simple and shorter code.

    # for saving the balance of performance, length of code and
    # simplicity we will check the list with only one loop, without
    # more functions.
    # The *and* and *or* keywords are optimized by defult and don't
    # evaluate the second argument if it is not needed.
    # There are more performant implementation!!! but I prefer this
    # implementation.

    result = [True, True, True, True]
    last = sequence[0]

    for x in sequence[1:]:
        result[1] = result[1] and last < x
        result[0] = result[1] or (result[0] and last <= x)
        result[3] = result[3] and last > x
        result[2] = result[3] or (result[2] and last >= x)
        last = x

    return result


def monotonicity_inverse(def_bool):
    """The function gets a booleans list as parameter which define
    the monotonicity of sequence and returns a list for example.
        - def_bool[0] := the sequence is monotonically increasing;
        - def_bool[1] := the sequence is strictly increasing;
        - def_bool[2] := the sequence is monotonically decreasing;
        - def_bool[3] := the sequence is strictly decreasing"""

    # Classic PROLOG function🤣

    if def_bool[1]:
        if def_bool[2] or def_bool[3] or not def_bool[0]:
            return None
        return [0, 1, 2, 3]

    if def_bool[3]:
        if def_bool[0] or def_bool[1] or not def_bool[2]:
            return None
        return [0, -1, -2, -3]

    if def_bool[0]:
        if def_bool[2]:
            return [0, 0, 0, 0]
        return [0, 1, 1, 2]

    if def_bool[2]:
        return [0, -1, -1, -2]

    return [0, 1, -1, 0]


def monotonicity_inverse_test():
    """Check monotonicity_inverse() function."""
    for x in range(2 ** 4):
        # trnsform the binary string of the number to bool list.
        param = [True if i == "1" else False for i in "{0:04b}".format(x)]
        sample = monotonicity_inverse(param)
        if sample == None:
            print(f"{param} -- None")
        else:
            test = sequence_monotonicity(sample)
            print(f"{param} -- {sample} {'✅' if test == param else '❎'}")
    # OUTPUT:
    # [False, False, False, False] -- [0, 1, -1, 0] ✅
    # [False, False, False, True] -- None
    # [False, False, True, False] -- [0, -1, -1, -2] ✅
    # [False, False, True, True] -- [0, -1, -2, -3] ✅
    # [False, True, False, False] -- None
    # [False, True, False, True] -- None
    # [False, True, True, False] -- None
    # [False, True, True, True] -- None
    # [True, False, False, False] -- [0, 1, 1, 2] ✅
    # [True, False, False, True] -- None
    # [True, False, True, False] -- [0, 0, 0, 0] ✅
    # [True, False, True, True] -- None
    # [True, True, False, False] -- [0, 1, 2, 3] ✅
    # [True, True, False, True] -- None
    # [True, True, True, False] -- None
    # [True, True, True, True] -- None




def my_map(l, f):
    return (f(i) for i in l)
def my_or(b1, b2):
    return b1 or b2
def my_and(b1, b2):
    return b1 and b2
def my_reduce(l, f, init):
    result = init
    for i in l:
        result = f(result, i)
    return result
def my_all(l, predicate):
    return my_reduce(my_map(l, predicate), my_and, True)
def my_any(l, predicate):
    return my_reduce(my_map(l, predicate), my_or, False)
def my_add(x,y):
    return x+y
def my_sum(l): 
    return my_reduce(l,my_add,0)
def min(x,y):
    if x < y: return x
    return y

# most efficient🙃
primes_for_asafi__primes_cache = [2,3,5,7]
primes_for_asafi__last_collect_cache = 3



def primes_for_asafi(n):
    global primes_for_asafi__primes_cache
    global primes_for_asafi__last_collect_cache
    primes = primes_for_asafi__primes_cache
    last_collect = primes_for_asafi__last_collect_cache
    if n <= len(primes):
        return primes[:n]
    # n2 = n ** 2
    n2 = n ** 2
    s = '1' * n2
    result = int(s,2)
    s = result
    i = 0


    while i < n2:
        # 2 -> 5
        p = primes[i]
        p1 = 2 ** (p - 1)
        p2 = p1 * 2
        # 0b...10000_10000_10000_10000
        x = 0
        for _ in range(n2//p + 1):
            x += 1
            x = x << p

        x = x >> 1
        x -= p1
        # 0b...01111_01111_01111_01111
        x = s ^ x
        result = result & x
        i += 1
        if len(primes) == i:
            current_state = result
            current_state =  current_state >> (last_collect ** 2)
            for j in range(last_collect ** 2, min(n**2, p ** 2)):
                if current_state & 1 == 1:
                    primes.append(j + 1)
                current_state = current_state >> 1
            last_collect = int(min(n, p))
            if n <= len(primes):
                primes_for_asafi__primes_cache = primes
                primes_for_asafi__last_collect_cache = last_collect
                return primes[:n]

for k in range(121):
    print(k, primes_for_asafi(k))