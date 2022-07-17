from typing import List
# Part 1

# Q6


class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.right, self.left = data, right, left


def tree_iter_level(root: Node, depth):
    if root is None:
        return
    if depth == 0:
        yield root.data
        return
    yield from tree_iter_level(root.left, depth - 1)
    yield from tree_iter_level(root.right, depth - 1)


def tree_iter(root, depth):
    for i in range(depth):
        yield from tree_iter_level(root, i)


root = Node(1,
            Node("A",
                 Node(2)),
            Node("B",
                 Node(3,
                      Node("C")),
                 Node(4)))

print(list(tree_iter(root, 3)))


# Q8
def is_legal_BST_core(root: Node):
    left = is_legal_BST_core(root.left) if root.left else None
    right = is_legal_BST_core(root.right) if root.right else None
    if left == False or right == False:
        return False
    if (left and left[1] > root.data) or (right and root.data >= right[0]):
        return False
    return (left[0] if left else root.data, right[1] if right else root.data)


def is_legal_BST(root: Node):
    if is_legal_BST_core(root):
        return True
    return False


is_legal_BST(Node(3, Node(8), Node(7)))
is_legal_BST(Node(3, Node(2), Node(7)))
is_legal_BST(Node(3, Node(2), Node(3)))
is_legal_BST(Node(3, Node(3), Node(7)))
is_legal_BST(Node(3, Node(3), Node(7, Node(2))))
is_legal_BST(Node(3, Node(3, None, Node(4)), Node(7)))


# Q7
class Cycle:
    def __init__(self, data):
        self.data = [data]
        self.index = 0

    def insert_next(self, data):
        self.data.insert(self.index+1, data)

    def rotate(self):
        self.index += 1
        self.index %= len(self.data)
        return self.data[self.index]

    def rotate_back(self):
        self.index -= 1
        self.index %= len(self.data)
        return self.data[self.index]

    def delete(self):
        if len(self.data) == 1:
            raise LookupError()
        del self.data[self.index]
        self.index %= len(self.data)

    def __str_item(self, ind):
        if ind == self.index:
            return f">{self.data[ind]}"
        return f"{self.data[ind]}"

    def __repr__(self):
        return "[" + ",".join(self.__str_item(i)
                              for i in range(len(self.data))) + "]"


class dNode:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data, self.next, self.prev = data, next, prev


class Cycle:
    def __init__(self, data):
        self._cur = dNode(data)
        self._cur.next = self._cur
        self._cur.prev = self._cur

    def insert_next(self, data):
        n = dNode(data, self._cur.next, self._cur)
        self._cur.next = n

    def rotate(self):
        self._cur = self._cur.next
        return self._cur.data

    def rotate_back(self):
        self._cur = self._cur.prev
        return self._cur.data

    def delete(self):
        if self._cur.next == self._cur:
            raise LookupError()
        self._cur.prev.next = self._cur.next
        self._cur.next.prev = self._cur.prev
        self._cur = self._cur.next

    def __repr__(self):
        node = self._cur
        res = f"[>{node.data}"
        node = node.next
        while node is not self._cur:
            res += f", {node.data}"
            node = node.next
        return res + "]"


c = Cycle(3)
c
c.insert_next(2)
c
c.insert_next(1)
c
print(c.rotate())
c
print(c.rotate())
c
print(c.rotate())
c
print(c.rotate())
c
c.delete()
c
print(c.rotate_back())
c

# Q8


def fix(d):
    def deco(f):
        def inner(*args, **kwargs):
            args = list(args)
            for key in sorted(d.keys()):
                args.insert(key, d[key])
            return f(*args, **kwargs)
        return inner
    return deco


@fix({0: 'a', 2: 'c'})
def g(x, y, z):
    return x+y+z


g("b")


# Part 2
# Q6
def min_time_core(workers: List[float], tasks: List[float]):
    if sum(tasks) == 0:
        yield max(workers)
        return
    task = tasks.pop()
    for i, _ in enumerate(workers):
        workers[i] += task
        yield from min_time_core(workers, tasks)
        workers[i] -= task
    tasks.append(task)


def min_time(num: int, tasks: List[float]):
    return min(min_time_core([0 for _ in range(num)], tasks))


min_time(4, [1, 2, 2.5, 2, 3, 6, 3, 3, 3])
