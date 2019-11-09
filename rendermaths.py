from math import sin, cos
import turtlemanager



def toactualpos(x, y, z):
    f = turtlemanager.fov / (z + 2)
    sx = x * f
    sy = y * f
    return sx, sy


def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x * c - y * s, x * s + y * c


def gotopoint(point,nodes):
    global counter
    item = nodes[point]
    x = item[0]
    y = item[1]
    z = item[2]
    x, z = rotate(x, z, 0)
    turtlemanager.t.goto(toactualpos(x, y, z))