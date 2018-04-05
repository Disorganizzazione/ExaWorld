import math
import pygame as pg
from GraphicHexagon import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------
if __name__ == "__main__":
    # TODO trovare il centro della finestra di pygame
    # TODO trovare il modo di sommare le coppie di coordinate ES: hex.center + (x,y)

    # Pygame initialization
    pg.init()
    displayInfo = pg.display.Info()
    window_width = 800
    window_height = 640
    hex_side = 40
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
    origin_center = (gameDisplay.get_width()/2, gameDisplay.get_height()/2)

    # Creating hexagons
    hex0 = GraphicHexagon(origin_center, hex_side)
    """
    hex1 = Hexagon((100, 100), 20, False)
    hex2 = Hexagon((200, 200), 40, True)
    hex3 = Hexagon((300, 300), 40, True, False, (1.0, 0.0, 0.0, 1.0))
    hex4 = Hexagon((100, 300), 30, True, False, (1.0, 0.0, 0.0, 1.0), 3)
    hex5 = Hexagon((300, 100), 30, False, True, (1.0, 0.0, 0.0, 1.0), 5)
    """
    center1 = (gameDisplay.get_width()/2, gameDisplay.get_height()/2 + hex_side*math.sqrt(3))
    hex1 = GraphicHexagon((origin_center[0] + 0, origin_center[1] + hex_side*math.sqrt(3)), hex_side)

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
        hex1.draw()

        # Update
        pg.display.flip()

    clock.tick(30)
