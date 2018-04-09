import math
import pygame as pg
from GraphicHexagon import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------
if __name__ == "__main__":

    # Pygame initialization
    pg.init()
    displayInfo = pg.display.Info()
    window_width = 800
    window_height = 640
    side = 40
    hex_side = side - 5
    gameDisplay = pg.display.set_mode((window_width, window_height), pg.OPENGL | pg.DOUBLEBUF)
    pg.display.set_caption("Prova 1")

    # OpenGL initialization
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 480, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LINE_SMOOTH)

    # Origin Hexagon center = center of the pygame window
    # TODO: capire perché height/4 e non height/2
    origin_center = (gameDisplay.get_width()/2, gameDisplay.get_height()/4)

    v3s = math.sqrt(3) * side / 2
    s3 = 3 * side / 2
    dirs = ['q', 'w', 'e', 'd', 's', 'a']
    coords = {'q': (-s3, v3s), 'w': (0, v3s*2), 'e': (s3, v3s),
              'd': (s3, -v3s), 's': (0, -v3s*2), 'a': (-s3, -v3s)}

    print(coords['q'])

    # Creating hexagons
    hex0 = GraphicHexagon(origin_center, hex_side)
    hexs = list()
    for i in range(6):
        x, y = hex0.get_center()
        print(x, y)
        center = (x + coords[dirs[i]][0],
                  y + coords[dirs[i]][1])
        print(center[0], center[1])

        hexs.append(GraphicHexagon((center[0], center[1]), hex_side))

    # Events loop
    clock = pg.time.Clock()
    while True:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            pg.quit()
            break

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the hexagons
        hex0.draw()
        for h in hexs:
            h.draw()

        # Update
        pg.display.flip()
        clock.tick(30)
