import pygame
import settings
#class used to grab the images out of the spritesheet
class Spritesheet(object):
    def __init__(self,file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self,x,y,width,height):
        #gets single sprite by getting the x and y location on ssprite sheet, and the width and height to cut out

        image = pygame.Surface([width,height]).convert()

        image.blit(self.sprite_sheet,(0,0), (x,y,width,height))

        image.set_colorkey(settings.ALPHA)

        return image