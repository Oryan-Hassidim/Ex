# Q1
def f1(n, m):
    liz = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            k = 1
            while k < len(liz) * len(liz[0]):
                k *= 2
                a, b = bla bla bla
                liz[a][b] = bla bla


def f2(n):
    i, j, k, x = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            for k in range(1, j):
                x += 1

# Q2


def go_back(lnk):
    if lnk:
        yield from go_back(lnk.next)
        yield lnk.data


def swap(lnk):
    while lnk != Lnk.empty or lnk.next != Lnk.empty:
        lnk.data, lnk.next.data = lnk.next.data, lnk.data
        lnk = lnk.next.next

# Q3


def add_pos_evens(liz):
    if len(liz) == 0:
        return 0
    else:
        if liz[0] % 2 == 0 and liz[0] > 0:
            return liz[0] + add_pos_evens(liz[1:])
        else:
            return add_pos_evens(liz[1:])


def high_low(n):
    if n < 10:
        return True
    if (n // 10) % 10 < n % 10:
        return False
    return high_low(n // 10)

# Q4


def add_matrics(A, B, dim):
    mat = [[0] * dim[1] for _ in dim[0]]

    for i, j in A.items():
        mat[i[0]][i[1]] += j

    for k, m in B:
        mat[k][m] += B[k, m]


def two_diags(mat):
    ...

    diag1, diag2 = 0, 0
    for r in range(len(mat)):
        diag1 += mat[r][r]
        diag2 += mat[r][len(mat) - r - 1]

# Q5


class Lnk:
    empty = ()

    def __init__(self, data, next=empty):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next:
            return f"Lnk({self.data}, {self.next})"
        return f"Lnk({self.data})"

### DO NOT EDIT ABOVE THIS LINE ###

    def __get_iter(self):
        cur = self
        while cur != Lnk.empty:
            yield cur.data
            cur = cur.next

    def __iter__(self):
        return self.__get_iter()

    def add_and_get(self, data):
        _next = self.next
        self.next = Lnk(data, _next)
        return self.next


def place_between(inter, linked_list):
    res = Lnk(None)
    cur = res
    prev = object()  # unique
    for x in linked_list:
        if prev == x:
            cur = cur.add_and_get(inter)
        cur = cur.add_and_get(x)
        prev = x
    return res.next


print(place_between(-7, Lnk(3, Lnk(3))))  # Lnk(3, Lnk(-7, Lnk(3)))
print(place_between(3, Lnk(3, Lnk(3))))  # Lnk(3, Lnk(3, Lnk(3)))
# Lnk(-7, Lnk(3, Lnk(-7, Lnk(3))))
print(place_between(-7, Lnk(-7, Lnk(3, Lnk(3)))))
# Lnk(7, Lnk(11, Lnk(7, Lnk(6, Lnk(11, Lnk(6, Lnk(11)))))))
print(place_between(11, Lnk(7, Lnk(7, Lnk(6, Lnk(6, Lnk(11)))))))
# Lnk(9, Lnk(10, Lnk(9, Lnk(10, Lnk(9)))))
print(place_between(10, Lnk(9, Lnk(9, Lnk(9)))))
ling = Lnk(11, Lnk(21))
print(place_between(5, ling))  # Lnk(11, Lnk(21))
lynk1 = Lnk(8)  # one element
lynk2 = place_between(-1, lynk1)
print(lynk1)  # Lnk(8)
print(lynk1 is not lynk2)  # True
print(place_between(0, Lnk.empty))


# Q6
def append_and_get(lst, x):
    lst.append(x)
    return lst


def no_twins_rec(n, x, y, enable_y=True):
    if n == 0:
        yield []
        return
    yield from (append_and_get(l, x) for l in no_twins_rec(n-1, x, y))
    if enable_y:
        yield from (append_and_get(l, y) for l in no_twins_rec(n-1, x, y, False))


def no_twins(n, x, y):
    if x != y:
        return list(no_twins_rec(n, x, y))
    # x == y
    if n == 0:
        return [[]]
    if n == 1:
        return [[x]]  # [x] == [y]
    return []


no_twins(3, 2, 5)


# Q7
class Tree:
    empty = ()

    def __init__(self, data, branches=[]):
        self.data = data
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            return f"Tree({self.data}, {self.branches})"
        return f"Tree({self.data})"

### DO NOT EDIT ABOVE THIS LINE ###

    def is_a_leaf(self):
        return len(self.branches) == 0


def reduce(f, iterable, default):
    res = default
    for x in iterable:
        res = f(res, x)
    return res


def prod(iterable):
    return reduce(lambda x, y: x*y, iterable, 1)


ops = {'*': prod, '+': sum}


def ops_to_leaves(iTree: Tree):
    if iTree.is_a_leaf():
        return iTree.data

    op = iTree.data
    iTree.data = ops[op](map(ops_to_leaves, iTree.branches))
    iTree.branches.insert(0, Tree(op))
    return iTree.data


iTree = Tree('*', [Tree(4), Tree('+', [Tree(4), Tree(5), Tree(6)])])
iTree
ops_to_leaves(iTree)
iTree


# Q8
class BinT:
    empty = ()

    def __init__(self, data, left=empty, right=empty):
        self.data = data
        self.left = left
        self.right = right

### DO NOT EDIT ABOVE THIS LINE ###

    def __repr__(self):
        if self.left == self.right == BinT.empty:
            return f"BinT({self.data})"
        if self.right == BinT.empty:
            return f"BinT({self.data}, {self.left})"
        return f"BinT({self.data}, {self.left if self.left else 'BinT.empty'}, {self.right})"


def pardes(lst, n=0):
    if n >= len(lst) or lst[n] is None:
        return BinT.empty

    left = pardes(lst, 2*n + 1)
    right = pardes(lst, 2*n + 2)
    return BinT(lst[n], left, right)


pardes([1, 2, 3])
pardes([1, None, 3])
pardes([1, 2, None])
pardes([1, 2, 3, 4, 5])


# Q9
def how_close(tree: Tree):
    if tree.is_a_leaf():
        return abs(tree.data)
    return min(abs(tree.data - sum(b.data for b in tree.branches)),
               min(map(how_close, tree.branches)))


how_close(Tree(1, [Tree(2), Tree(3)]))
how_close(
    Tree(1, [
        Tree(2),
        Tree(3, [
            Tree(1),
            Tree(2)])]))


# Q10
def single_rep(lnk: Lnk):
    if lnk == Lnk.empty:
        return 0
    if lnk.next == Lnk.empty or lnk.data != lnk.next.data:
        _next = lnk.next
        lnk.next = Lnk(lnk.data, _next)
        return 1 + single_rep(lnk.next.next)

    data = lnk.data
    while lnk != Lnk.empty and lnk.data == data:
        lnk = lnk.next
    return single_rep(lnk)


lnk = Lnk(1, Lnk(1, Lnk(3, Lnk(3))))
single_rep(lnk)
lnk

lnk = Lnk(1, Lnk(1, Lnk(2, Lnk(3, Lnk(3)))))
single_rep(lnk)
lnk

lnk = Lnk(1, Lnk(2, Lnk(2, Lnk(3, Lnk(4)))))
single_rep(lnk)
lnk

lnk = Lnk(1, Lnk(2, Lnk(2, Lnk(2, Lnk(4)))))
single_rep(lnk)
lnk

lnk = Lnk(1)
single_rep(lnk)
lnk
