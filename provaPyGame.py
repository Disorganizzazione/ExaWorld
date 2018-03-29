
import pygame
import colorsys

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Prova')

#Colors
white = (255,255,255)
red = (255,0,0)

gameDisplay.fill(white)
rekt = [300,300, 30,30]
gameDisplay.fill(red, rekt)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(gameDisplay, (0, 0, 0), [200,200,30,30], 1)
    pygame.display.update()


pygame.quit()
quit()
