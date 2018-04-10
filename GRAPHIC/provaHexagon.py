
import math
import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from GraphicHexagon import *

# ----------------------------------------------------------
# Entry Point
# ----------------------------------------------------------
if __name__ == "__main__":

    # Pygame initialization
    pg.init()
    displayInfo = pg.display.Info()
    window_width = displayInfo.current_w - 50
    window_height = displayInfo.current_h - 50
    side = 30
    hex_side = math.floor(side*9/10)
    gameDisplay = pg.display.set_mode((window_width, window_height), pg.OPENGL | pg.DOUBLEBUF | pg.OPENGLBLIT)
    pg.display.set_caption("Prova 1")

    # OpenGL initialization
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, window_height, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LINE_SMOOTH)

    # Origin Hexagon center = center of the pygame window
    origin_center = (gameDisplay.get_width()/2, gameDisplay.get_height()/2)

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

    # Prova: da Exa a GraphicHexagon
    # exo = Exa(2,2,-4)
    exo = (2,2,-4)
    # xello = Xel(exo)
    x, y = hex0.get_center()
    x = x + side*3/2*exo[1]
    y = y + side*math.sqrt(3)*(exo[2] + exo[1]/2)
    hexago = GraphicHexagon((x, y), hex_side)

    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pg.font.SysFont("monospace", 30)
    # render text
    #label = myfont.render("Some text!", True, (255, 255, 255))
    #gameDisplay.blit(label, hexago.get_center())


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
        hexago.draw()
        label = myfont.render("Some text!", True, (255, 255, 0))
        gameDisplay.blit(label, hexago.get_center())
        print(label)

        # Update
        pg.display.flip()
        clock.tick(30)
