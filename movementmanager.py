import turtlemanager

playerzpos=0
forward=False
def processmovement():
    global forward,playerzpos
    if forward:
        playerzpos += 1
    forward=False

def wdown():
    global forward
    forward=True
def wup():
    global forward
    forward=False



turtlemanager.screen.onkeypress(wdown,"w")
turtlemanager.screen.onkey(wup, "w")
turtlemanager.screen.listen()