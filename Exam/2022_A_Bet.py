from typing import Any, List, Dict
from dataclasses import dataclass

## Part 1
# Q7
from email import header


def get_k_tuples(it, k):
    lst = []
    for x in it:
        lst.append(x)
        if len(lst) == k:
            yield tuple(lst)
            del lst[0]

print(list(get_k_tuples(range(14),3)))


# Q9
def xyz_core(x,y,z):
    if x==y==z==0:
        yield ''
    if x>0:
        yield from ('x'+s for s in xyz_core(x-1,y,z))
    if y>0:
        yield from ('y'+s for s in xyz_core(x,y-1,z))
    if z>0:
        yield from ('z'+s for s in xyz_core(x,y,z-1))

def xyz(x,y,z):
    return list(set(xyz_core(x,y,z)))


# Q7
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

def find_max_sum_pair(head:Node):
    n, node = 0, head
    while node is not None:
        n, node = n+1, node.next

    i, res, node = 0, [], head
    while i<=n-i-1:
        node2 = node
        for _ in range(n-2*i-1):
            node2 = node2.next
        res.append(node.data + node2.data)
        res[:] = (max(res),)
        i, node = i+1, node.next
    return res[0]

head = Node(1, Node(2, Node(1, Node(3, Node(1)))))
find_max_sum_pair(head)

## Part 2
# Q8
@dataclass
class Node:
    data:Any
    children: List[Node]

def leaves(node:Node, d:int):
    if not node.children:
        yield d
        return
    d += 1
    for child in node.children:
        yield from leaves(child, d)

def check_tree(tree:Node):
    res = set()
    for leaf in leaves(tree, 0):
        res.add(leaf % 2)
        if len(res) > 1:
            return None
    return res.pop()

tree = Node(1, [Node(1,[]), Node(1, [Node(1, [])])])
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

f(1,2,3)
f(1,2)

