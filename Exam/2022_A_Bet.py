from typing import Any, List, Dict, Tuple
from dataclasses import dataclass

# Part 1
# Q7

def get_k_tuples(it, k):
    lst = []
    for x in it:
        lst.append(x)
        if len(lst) == k:
            yield tuple(lst)
            del lst[0]


print(list(get_k_tuples(range(14), 3)))


# Q9
def xyz_core(x, y, z):
    if x == y == z == 0:
        yield ''
    if x > 0:
        yield from ('x'+s for s in xyz_core(x-1, y, z))
    if y > 0:
        yield from ('y'+s for s in xyz_core(x, y-1, z))
    if z > 0:
        yield from ('z'+s for s in xyz_core(x, y, z-1))


def xyz(x, y, z):
    return list(set(xyz_core(x, y, z)))


# Q7
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def find_max_sum_pair(head: Node):
    n, node = 0, head
    while node is not None:
        n, node = n+1, node.next

    i, res, node = 0, [], head
    while i <= n-i-1:
        node2 = node
        for _ in range(n-2*i-1):
            node2 = node2.next
        res.append(node.data + node2.data)
        res[:] = (max(res),)
        i, node = i+1, node.next
    return res[0]


head = Node(1, Node(2, Node(1, Node(3, Node(1)))))
find_max_sum_pair(head)

# Part 2
# Q7


def intersect(intervals: List[Tuple[int, int]], points: List[int]):
    axis = {}
    for a, b in intervals:
        axis[a] = axis.get(a, 0) + 1
        axis[b] = axis.get(b, 0) - 1
    for p in points:
        if p in axis:
            return True
        axis[p] = "check"

    keys = sorted(axis)
    cur = 0
    for key in keys:
        val = axis[key]
        if val == "check":
            if cur > 0:
                return True
        else:
            cur += val
    return False


intersect([(3.5, 4.5), (-1, 2), (3, 4)], [2.5, 5.5])  # False
intersect([(1, 2), (3, 4)], [1])  # True
intersect([(1, 2), (3, 4)], [7, 3.5])  # True


# Q8
@dataclass
class Node:
    data: Any
    children: List[Any]


def leaves(node: Node, d: int):
    if not node.children:
        yield d
        return
    d += 1
    for child in node.children:
        yield from leaves(child, d)


def check_tree(tree: Node):
    res = set()
    for leaf in leaves(tree, 0):
        res.add(leaf % 2)
        if len(res) > 1:
            return None
    return res.pop()



def get_leaves(node, depth):
    if len(node.children) == 0:
        yield depth
    for child in node.children:
        yield from get_leaves(child, depth + 1)

def check_tree(node):
    res = set()
    for x in get_leaves(node, 0):
        res.add(x % 2)
        if len(res) > 1:
            return None
    return res.pop()

tree = Node(1, [Node(1, []), Node(1, [])])
print(check_tree(tree))

# Q9
def uncurry(n):
    def dec(f):
        def inner(*args):
            if len(args) != n:
                raise TypeError
            res = f
            for x in args:
                res = res(x)
            return res
        return inner
    return dec


@uncurry(3)
def f(x):
    return lambda y: lambda z: x+y+z


f(1, 2, 3)
f(1, 2)


# circular list
class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        cur = self.next
        s = f"{self.data} -> "
        while cur is not self:
            s += f"{cur.data} -> "
            cur = cur.next
        s += f"{self.data} -> ..."
        return s

def rev(node):
    prev = node
    cur = node.next
    while cur is not node:
        _next = cur.next
        cur.next = prev
        prev = cur
        cur = _next
    cur.next = prev

node = Node(7, Node(5, Node(7, Node(3))))
node.next.next.next.next = node
print(node)
rev(node)
print(node)

