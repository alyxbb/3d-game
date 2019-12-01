import rendermaths
import turtlemanager


def drawshape(nodes, lines):
    for line in lines:
        turtlemanager.t.penup()
        rendermaths.gotopoint(line[0], nodes)
        turtlemanager.t.pendown()
        rendermaths.gotopoint(line[1], nodes)
