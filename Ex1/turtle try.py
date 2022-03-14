#############################################################
# FILE : Ex.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex1 2022
# DESCRIPTION: A simple program that prints "Hello World!" to
# the standard output (screen).
#############################################################

# from turtle import *

# big = 200
# step = 20

# clear()

# speed(5000)

# pu()
# bk(big / 2)
# rt(90)
# bk(big / 2)
# lt(90)
# pd()

# for j in [1,2,3,4,5,6]:
#    print(j)
#    for s in range(big, 0, -step):
#        for i in range(1,5):
#            forward(s)
#            right(90)
#        pu()
#        fd(step/2)
#        rt(90)
#        fd(step/2)
#        lt(90)
#        pd()

#    pu()
#    rt(15)
#    bk(big / 2)
#    rt(90)
#    bk(big / 2)
#    lt(90)
#    pd()


import array as arr
from array import *

lst = [300, 301, 302, 303]
for x in lst:
    print(x)
    print(id(x))

arr1 = array("I", (x for x in range(10)))
bs = array.tobytes(arr1)
print(bs)
for x in arr1:
    print(x)
    print(id(x))

from pipe import select, where

arr = [1, 2, 3, 4, 5]
lst = list(arr
     | where (lambda x: x % 2 == 0)
     | select (lambda x: x *2))

print(lst)