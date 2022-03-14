#############################################################
# FILE : Ex.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex1 2022
# DESCRIPTION: A simple Program that draws flowers with
# python turtle like a LOGO app.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: https://docs.python.org/3/library/turtle.html
# NOTES: I used the short names of Turtle class function
#        like rt()<=>right(), fd()<=>forward() and so on...
#############################################################

from turtle import *


def draw_petal():
    """Draws single petal on the screen.
    Starts from current point of the turtle."""
    for i in [1, 2]:
        fd(30)
        rt(45)
        fd(30)
        rt(135)


def draw_flower():
    """Draws single flower on the screen.
    Starts from current point of the turtle."""
    lt(45)
    for x in range(4):
        draw_petal()
        lt(90)
    lt(135-90)
    fd(150)


def draw_flower_and_advance():
    """Draws single flower on the screen and advances
    the turtle to the position of the next flower.
    Starts from current position of the turtle."""
    draw_flower()
    rt(90)
    pu()
    fd(150)
    rt(90)
    fd(150)
    lt(90)
    pd()


def draw_flower_bed():
    """Draws 3 flowers on the screen.
    Starts from (0,0)."""
    pu()
    fd(200)
    lt(180)
    pd()
    for i in range(3):
        draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    done()