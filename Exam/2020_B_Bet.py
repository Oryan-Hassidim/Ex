import math


def eq_vals(func, lzt):
    res = {}
    for x in lzt:
        i = func(x)
        lst = res.get(i, [])
        lst.append(x)
        res[i] = lst
    return list(res.values())


lzt = list(range(1, 14))


def func(x): return (x % 3)*2 - x % 2


eq_vals(func, lzt)


def opti(i, j, table, depth, so_far=0):
    if j >= len(table[i]):
        return
    so_far += table[i][j]
    if depth == 1:
        yield so_far
        return
    yield from opti(i+1, j, table, depth-1, so_far)
    yield from opti(i+1, j+1, table, depth-1, so_far)


def opti_sum(table):
    for n, _ in enumerate(table):
        yield max(o
                  for j in range(len(table[0]))
                  for o in opti(0, j, table, n+1))


table = [[4, 2, 3],
         [2, 3, 4, 1, 6],
         [3, 4, 1, 5, 9, 4, 3]]

g = opti_sum(table)
next(g)  # 4
next(g)  # 7
next(g)  # 13
