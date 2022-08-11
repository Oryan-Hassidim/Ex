# Q2
def all_sums_rec(num, bound, so_far):
    if num == 0:
        yield so_far
        return
    if num < 0:
        return
    for x in range(bound, 0, -1):
        so_far.append(x)
        yield from all_sums_rec(num - x, x, so_far)
        so_far.pop()


def all_sums(num, bound):
    yield from (" + ".join(map(str, s))
                for s in all_sums_rec(num, bound, []))

list(all_sums(5, 3))


