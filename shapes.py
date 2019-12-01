import drawer


def drawcuboid(size, coordinates):
    x1, y1, z1 = coordinates
    lx, ly, lz = size
    x2 = x1+lx
    y2 = y1+ly
    z2 = z1+lz
    nodes = []
    lines = [[0, 2], [0, 4], [2, 6], [4, 6],
             [1, 3], [1, 5], [3, 7], [5, 7],
             [0, 1], [2, 3], [4, 5], [6, 7]]
    for xpos in [x1, x2]:
        for ypos in [y1, y2]:
            for zpos in [z1, z2]:
                nodes.append([xpos, ypos, zpos])
    drawer.drawshape(nodes, lines)
