import shapes
import turtlemanager
import movementmanager
import time


def mainloop():
    turtlemanager.t.clear()
    movementmanager.processmovement()   
    shapes.drawcuboid([1,1,1],[0,0,0])
    turtlemanager.screen.update()
    turtlemanager.screen.ontimer(mainloop,0)


mainloop()

turtlemanager.screen.mainloop()
