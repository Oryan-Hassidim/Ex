def rooms_rec(i, j, rooms):
    if rooms[i, j][4]:
        return
    rooms[i, j][4] = True
    if not rooms[i, j][0]:
        rooms_rec(i-1, j, rooms)
    if not rooms[i, j][1]:
        rooms_rec(i, j+1, rooms)
    if not rooms[i, j][2]:
        rooms_rec(i+1, j, rooms)
    if not rooms[i, j][3]:
        rooms_rec(i, j-1, rooms)


def main():
    h = int(input("height: "))
    w = int(input("width: "))

    rooms = {(i, j): [False]*5 for i in range(h) for j in range(w)}

    for i in range(h):
        codes = [int(c) for c in input().split(" ")]
        for j, code in enumerate(codes):
            for a in range(3, -1, -1):
                if code >= 2**a:
                    code -= 2**a
                    rooms[i, j][a] = True

    n = 0
    for i in range(h):
        for j in range(w):
            if not rooms[i, j][4]:
                rooms_rec(i, j, rooms)
                n += 1
    print(n)

# main()


def same_char_helper(str1, k):
    n = k
    while n < len(str1) and str1[n] == str1[k]:
        n += 1
    return n - k


def describe_str_helper(str1, k):
    if k >= len(str1):
        return ''
    times = same_char_helper(str1, k)
    return f'{str1[k]}{times}{describe_str_helper(str1, k+times)}'


def describe_str_helper(str1, k, n, last=None):
    if k == len(str1):
        return f'{last}{n}'
    if not last:
        return describe_str_helper(str1, k+1, 1, str1[k])
    if str1[k] == last:
        return describe_str_helper(str1, k+1, n+1, last)
    return f'{last}{n}{describe_str_helper(str1, k+1, 1, str1[k])}'


def describe_str(str1):
    return describe_str_helper(str1, 0, 0)


describe_str('aabbcccccgg')


def guess_pass(pwd, txt: str):
    if pwd == '':
        return []
    c = pwd[0]
    if c not in txt:
        return False
    k = txt.index(c)
    rest = guess_pass(pwd[1::], txt[k+1::])
    if rest is False:
        return False
    return [k] + [i+k+1 for i in rest]


guess_pass('abc-123', 'a1b2c34/-1x2gh3n')
guess_pass('abc-123', 'a12c34/-1x2gh3n')


class Link:
    empty = ()

    def __init__(self, data, next=empty):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next is Link.empty:
            return "Link({})".format(self.data)
        else:
            return "Link({}, {})".format(self.data, self.next)

######### DO NOT EDIT ABOVE THIS LINE! #########


def de_comp(n, base_lst):
    if base_lst == Link.empty:
        if n == 0:
            return Link.empty
        raise ArithmeticError
    if n >= base_lst.data:
        return Link(base_lst.data, de_comp(n-base_lst.data, base_lst.next))
    return de_comp(n, base_lst.next)

twos = Link(32, Link(16, Link(8, Link(4, Link(2, Link(1))))))
fibos = Link(34,(Link(21, Link(13, Link(8, Link(5, Link(3, Link(2,Link(1)))))))))

#print(de_comp(9, twos),de_comp(45,twos),de_comp(9, fibos),de_comp(30, fibos),de_comp(41, fibos),de_comp(0, fibos), sep='\n')
#de_comp(71, twos)



def reduce(iterable, func, default):
    res = default
    for x in iterable:
        res = func(res, x)
    return res

def all(iterable):
    return reduce(iterable, lambda x,y: x and y, True)
def any(iterable):
    return reduce(iterable, lambda x,y: x or y, False)
def sum(iterable):
    return reduce(iterable, lambda x,y: x+y, 0)
def prod(iterable):
    return reduce(iterable, lambda x,y: x*y, 1)


chars = '0123456789ABCDEF'
def convert(n:int, b:int) -> str:
    if n == 0:
        return ''
    return  f'{convert(n//b, b)}{chars[n%b]}'

print(convert(14,14))
print(convert(428,14))
