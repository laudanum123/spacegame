import pygame
import src.utils
import operator
import math

# CONSTANTS FOR STARSHIP BEHAVIOR
DRAG = 0.1  # How fast does the starship lose its speed
ACCEL = 0.2  # How fast does the sharship accelerate

class starship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = src.utils.load_image('enterprise.png',(0,0,0))
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()


    def update(self):
        self.flight_control()
        # move the ship to new position
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.wrap_around()

    def flight_control(self):
        # handles everything related to simple starship flight
        # check if direction buttons are pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            # up
            self.speedy += -ACCEL
        elif keystate[pygame.K_LEFT]:
            # left
            self.speedx += -ACCEL
        elif keystate[pygame.K_DOWN]:
            # down
            self.speedy += ACCEL
        elif keystate[pygame.K_RIGHT]:
            # right
            self.speedx += ACCEL
        else:
            # if no button is pressed slowly reduce speed
            if self.speedy > DRAG:
                self.speedy += -DRAG
            elif self.speedy < -DRAG:
                self.speedy += DRAG
            if self.speedx > DRAG:
                self.speedx += -DRAG
            elif self.speedx < -DRAG:
                self.speedx += DRAG

    def wrap_around(self):
        # if starship leaves the screen make it reappear at opposite side

        if self.rect.left > self.WIDTH+20:
            self.rect.right = 0
        if self.rect.right < -20:
            self.rect.left = self.WIDTH
        if self.rect.top > self.HEIGHT+20:
            self.rect.bottom = 0
        if self.rect.bottom < -20:
            self.rect.top = self.HEIGHT
