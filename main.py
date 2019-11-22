import os, sys, pygame
import src.starship
from pygame.locals import *
import operator

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

WIDTH = 1200
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Starship AI')
clock = pygame.time.Clock()


# Create Star Background
background = pygame.image.load('res/stars.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background = background.convert()

#screen.blit(background, (0,0))


starship = src.starship.starship()
allsprites = pygame.sprite.RenderPlain(starship)


pygame.display.flip()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    allsprites.update()

    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()
