from math import sin, cos
import turtlemanager
import movementmanager


def toactualpos(x, y, z):
    calcz = z+(movementmanager.playerzpos/20)
    if calcz <= 0:
        return 0, 0, False
    f = turtlemanager.fov / calcz

    sx = (x+(movementmanager.playerxpos/20)) * f
    sy = (y+(movementmanager.playerypos/20)) * f
    return sx, sy, True


def rotate(x, y, r):
    s, c = sin(r), cos(r)
    return x * c - y * s, x * s + y * c


def gotopoint(point, nodes):
    item = nodes[point]
    x = item[0]
    y = item[1]
    z = item[2]
    x, z = rotate(x, z, 0)
    acx, acy, render = toactualpos(x, y, z)
    if render:
        turtlemanager.t.goto(acx, acy)
