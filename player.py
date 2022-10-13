import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, color):
        super().__init__()
       
        self.images = []
        for i in range ( 1, 10):
            #takes in image and places it into array
            img = pygame.image.load(os.path.join('maps','Hobbit - run' + str(i) + '.png')).convert() 
            self.images.append(img)
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x,pos_y]

        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames

    def control(self,x, y):
        #player movement
        self.movex += x
        self.movey += y

    def update(self):
        #updates position of sprite
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left (face left and animates through the array while flipping image)
        if self.movex < 0:
            self.frame += 1
            if self.frame > 6*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right (doesnt flip image and goes through the animation while moving)
        if self.movex > 0:
            self.frame += 1
            if self.frame > 6*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]