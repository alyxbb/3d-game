import turtlemanager

playerzpos = 0
playerxpos = 0
playerypos = 0


def processmovement():
    global playerzpos, playerxpos, playerypos
    if w_key.down:
        playerzpos += 1
    if s_key.down:
        playerzpos -= 1
    if a_key.down:
        playerxpos += 1
    if d_key.down:
        playerxpos -= 1
    if q_key.down:
        playerypos += 1
    if e_key.down:
        playerypos -= 1


class WatchedKey:
    def __init__(self, key):
        self.key = key
        self.down = False
        turtlemanager.screen.onkeypress(self.press, key)
        turtlemanager.screen.onkeyrelease(self.release, key)

    def press(self):
        self.down = True

    def release(self):
        self.down = False


w_key = WatchedKey('w')
a_key = WatchedKey('a')
s_key = WatchedKey('s')
d_key = WatchedKey('d')
q_key = WatchedKey('q')
e_key = WatchedKey('e')

turtlemanager.screen.listen()
