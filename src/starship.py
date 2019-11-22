import pygame
import src.utils
import operator
import math

class starship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = src.utils.load_image('enterprise.png',(0,0,0))
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # check if direction buttons are pressed
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
            # up
            self.speedy += -.2
        elif keystate[pygame.K_LEFT]:
            # left
            self.speedx += -.2
        elif keystate[pygame.K_DOWN]:
            # down
            self.speedy += .2
        elif keystate[pygame.K_RIGHT]:
            # right
            self.speedx += .2
        else:
            # if no button is pressed slowly reduce speed
            if self.speedy > 0.2:
                self.speedy += -0.2


        # if no button is pressed the ship slowly loses speed
        if self.engine_on == 0:
            reduction_matrix = [0,0]
            reduction_matrix[0] = math.copysign(.2, self.speed[0])
            reduction_matrix[1] = math.copysign(.2, self.speed[1])
            self.speed = tuple(map(operator.sub, self.speed, reduction_matrix))

        # set the new speed
        self.speed = tuple(map(operator.add, self.speed, self.accel))

        # move the ship to new position
        newpos = self.rect.move(self.speed)
        self.rect = newpos
