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

myFont = pygame.font.SysFont("Arial", 18)
accTextLabel = myFont.render("Acceleration:", 1, (255,255,255))
speedTextLabel = myFont.render("Speed:", 1, (255,255,255))
accel = (0,0)

pygame.display.flip()

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    accValLabel = myFont.render(str(accel), 1, (255, 255, 255))
    speedValLabel = myFont.render(str(starship.speed), 1, (255, 255, 255))

    allsprites.update()

    screen.blit(background, (0, 0))
    screen.blit(accTextLabel, (520, 20))
    screen.blit(speedTextLabel, (520, 60))
    screen.blit(speedValLabel, (600, 60))
    screen.blit(accValLabel, (600, 20))
    allsprites.draw(screen)
    pygame.display.flip()
