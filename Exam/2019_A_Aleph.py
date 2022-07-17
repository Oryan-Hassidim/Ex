

# 1
def make_closed(dic):
    remove = set()
    closed = set()
    temp = set()

    for key in dic:
        if key in remove or key in closed:
            continue
        while (key not in remove) and (key not in closed) and (key not in temp) and (key in dic):
            temp.add(key)
            key = dic[key]
        if key in remove or key not in dic:
            remove.update(temp)
        else:  # closed or temp
            closed.update(temp)
        temp.clear()
    for key in remove:
        del dic[key]


dic = {1: 2, 2: 3, 3: 1, 7: 7}
make_closed(dic)
dic
dic[8] = 9
dic[11] = 8
dic[5] = 6
dic[6] = 7
make_closed(dic)
dic

# 2
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.data} <-> {self.next}"


def weave(a, b):
    def iter2():
        for i in range(len(a)):
            yield a[i]
            yield b[i]
    pre, head = None, None
    for x in iter2():
        node = Node(x)
        node.prev = pre
        if pre is not None:
            pre.next = node
        else: 
            head = node
        pre = node
    return head


print(weave([1, 7, 5], [2, 4, 3]))


# 5
def make_stack():
    stack = []
    def s(*args):
        if len(args) == 0:
            return stack.pop()
        stack.append(args[0])
    return s

s = make_stack()
s(1)
s(2)
m = make_stack()
m(1)
m(2)
s()
s()
s() # error!!





