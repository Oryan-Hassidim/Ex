class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next is not None:
            return f"{self.data} -> {self.next}"
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __repr__(self):
        if self.head is None:
            return "[||]"
        return f"[|{self.head}|]"

    def delete_at_loc(self, del_loc):
        cur = self.head
        for i in range(del_loc-1):
            cur = cur.next
        cur.next = cur.next.next
        self.len -= 1


#lst = LinkedList()
#lst.head = Node(0)
#lst.head.next = Node(1)
#lst.head.next.next = Node(2)
#lst.head.next.next.next = Node(3)

#lst
#lst.delete_at_loc(1)
#lst


# Q6
brackets = set("(){}[]")

open = list("({[")
close = list(")}]")

def balanced_rec(lst:list):
    if len(lst) == 0:
        return True
    first = lst.pop()
    if first not in open:
        return False

    while len(lst) > 0 and lst[-1] in open:
        if not balanced_rec(lst):
            return False
    
    c = lst.pop()
    return c in close and close.index(c) == open.index(first)

def balanced(str1):
    lst = [')']
    lst.extend(c for c in str1[::-1] if c in brackets)
    lst.append('(')
    return balanced_rec(lst)
    
def semi_balanced(s:str):
    return (s.count('(') == s.count(')')
            and s.count('[') == s.count(']')
            and s.count('{') == s.count('}'))
zt = 'lu{v yf;[oh(uc)bk]bd[qn(kf);cb]j9}ry()'
print(balanced(zt))
zt = 'lu{v yf;[oh(uc)bk]bd[qn(kf);cb]j9}ry(]'
print(balanced(zt))
zt = '(({}((}))))'
print(balanced(zt))
zt1 = 'lu{v yf;[oh(uc[bk]bd[qn(kf);cb]j9}ry'
print(balanced(zt1))


# Q8
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

def de_comp(n, base_lst:Link):
    if base_lst == Link.empty:
        if n != 0:
            raise ArithmeticError
        return Link.empty

    b = base_lst.data
    if n >= b:
        return Link(b, de_comp(n-b, base_lst.next))
    return de_comp(n, base_lst.next)



    
twos = Link(32, Link(16, Link(8, Link(4, Link(2, Link(1))))))
fibos = Link(34,(Link(21, Link(13, Link(8, Link(5, Link(3, Link(2,Link(1)))))))))

#print(de_comp(9, twos),de_comp(45,twos),de_comp(9, fibos),de_comp(30, fibos),de_comp(41, fibos),de_comp(0, fibos), sep='\n')
#de_comp(71, twos)


# Q7
class Tree:
    def __init__(self, data, branches=[]):
        self.data = data
        self.branches = list(branches) 

    def is_a_leaf(self):
        return not self.branches
        
######### DO NOT EDIT ABOVE THIS LINE! #########

def reduce(iterable, op, defult):
    res = defult
    for x in iterable:
        res = op(res, x)
    return res
    
def add(iterable):
    return reduce(iterable, lambda x,y: x+y, 0)
    
def mult(iterable):
    def add_mult(x,y):
        if x > y:
            y,x = x,y
        res = 0
        for _ in range(x):
            res += y
        return res
    return reduce(iterable, add_mult, 1)
    
ops = {'+': add, '*': mult}


def plus_it(t):
    if t.is_a_leaf():
        return t.data
    return ops[t.data](map(plus_it, t.branches))
    
    
    #return ops[t.data](plus_it(b) for b in t.branches)
 

    
t1 = Tree('*', [Tree(2), Tree(3)])
print(plus_it(t1))

t2 = Tree('+',[Tree(8), Tree(7)])  
print(plus_it(t2))

t3 = Tree('*',[Tree(5), Tree(7)]) 
print(plus_it(t3))

t4 = Tree('+',[t1, t2, t3])
print(plus_it(t4))

t5 = Tree('*', [Tree(11), Tree(12), t4, Tree(13)])
print(plus_it(t5))    
    



#NETA
class Tree:
    def __init__(self, data, branches=[]):
        self.data = data
        self.branches = list(branches)

    def is_a_leaf(self):
        return not self.branches


######### DO NOT EDIT ABOVE THIS LINE! #########
def plus_it_helper(t):
    if t.is_a_leaf():
        return t.data
    res_so_far = None
    for branch in t.branches:
        if res_so_far is None:
            res_so_far = plus_it_helper(branch)
        elif t.data == "+":
            res_so_far += plus_it_helper(branch)
        elif t.data == "*":
            replace_res_so_far = 0
            for i in range(res_so_far):
                replace_res_so_far += plus_it_helper(branch)
            res_so_far = replace_res_so_far
    return res_so_far


def plus_it(t):
    return plus_it_helper(t)


t1 = Tree('*', [Tree(2), Tree(3)])
print(plus_it(t1))
#6

t2 = Tree('+',[Tree(8), Tree(7)])
print(plus_it(t2))

#15

t3 = Tree('*',[Tree(5), Tree(7)])
print(plus_it(t3))
#35

t4 = Tree('+',[t1, t2, t3])
print(plus_it(t4))
#56

t5 = Tree('*', [Tree(11), Tree(12), t4, Tree(13)])
print(plus_it(t5))
#96096

t6 = Tree('*', [Tree(2), Tree(-1), Tree(3), t4])
plus_it(t6)

# Q10
from math import gcd
def lcm(a, b): 
    return abs(a // gcd(a, b) * b) #intentionally fails when gcd(a,b)==0

class Frac:
    
    def __init__(self, mone, mahane):
        self.mone = mone
        
        if mahane == 0:
            raise ZeroDivisionError
            
        self.mahane = mahane
        self._reduce()
    ######### DO NOT EDIT ABOVE THIS LINE! #########

    def _reduce(self):
        m,n = self.mone, self.mahane
        sgn = -1 if m*n<0 else 1
        g = gcd(abs(m), abs(n))
        self.mone = sgn * (abs(m) // g)
        self.mahane = abs(n) // g

    def __add__(self, other):
        ...
        
    def __sub__(self, other):
        ...

    def __mul__(self, other):
        ...
        
    def __truediv__(self, other):
        ...

    def __pow__(self, power):
        return Frac(self.mone**power, self.mahane**power)
        
    def __eq__(self, other):
        ...

    def __ge__(self, other):
        ...

    def __str__(self):
        m,n = self.mone, self.mahane
        sgn = "-" if m*n < 0 else ""
        m,n = abs(m), abs(n)
        whole = f"{m//n} " if m>n else ""
        return f"{sgn}{whole}{m%n}/{n}"

    def __repr__(self):
        return str(self)




