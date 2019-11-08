import turtle
import time
from math import cos, sin
from random import randint
screen=turtle.Screen()
fov = 100
counter = 0
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen.tracer(0, 0)

nodes = [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]

lines = [[0, 2], [0, 4], [2, 6], [4, 6],
         [1, 3], [1, 5], [3, 7], [5, 7]
    , [0, 1], [2, 3], [4, 5], [6, 7]]


def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x * c - y * s, x * s + y * c


def renderframe():
    t.clear()
    draw()


def draw():
    for line in lines:
        t.penup()
        gotopoint(line[0])
        t.pendown()
        gotopoint(line[1])


def gotopoint(point):
    global counter
    item = nodes[point]
    x = item[0]
    y = item[1]
    z = item[2]
    x, z = rotate(x, z, counter)
    t.goto(toactualpos(x, y, z))


def toactualpos(x, y, z):
    f = fov / (z + 2)
    sx = x * f
    sy = y * f
    return sx, sy


while True:
    renderframe()
    counter += 0.02
    t.pensize(20)
    t.pencolor("red")
    screen.update()