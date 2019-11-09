import shapes
import turtlemanager
import movementmanager
import time


while True:
    turtlemanager.screen.tracer(0,0)
    movementmanager.processmovement()
    shapes.drawcuboid([1,1,1],[0,0,0])
    turtlemanager.screen.update()
    time.sleep(2)
