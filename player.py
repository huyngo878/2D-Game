import pygame
from support import *
from settings import *
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

       
        self.status = 'down'
        self.frame_index = 0
        #uses direction as index for us to organize the files for the animations
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 
                            'right_idle':[], 'left_idle': [], 'up_idle': [], 'down_idle': []}

        sprite_sheet = Spritesheet("walkingss.png")

        index = 0
        #adds down facing animation sprites 
        for x in range(4):
            image = sprite_sheet.get_image(index,0,14,16)
            self.animations['down'].append(image)
            index = index + 14
        #adds left facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index,0,14,16)
            self.animations['left'].append(image)
            index = index + 14
        #adds right facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index,0,14,16)
            self.animations['right'].append(image)
            index = index + 14
        #adds up facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index,0,14,16)
            self.animations['up'].append(image)
            index = index + 14

        # Window Setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # Movement Setup (Direction, Speed, etc.)
        self.direction = pygame.math.Vector2() # Default value for Vector2 is (0, 0)
        self.pos = pygame.math.Vector2(self.rect.center) #Sets the position of the player to be the center
        self.speed = 300 #Speed of the Player


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0



        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self, dt):

        #Normalizing a Vector to set the diagonal direction to 1 instead of 2 which makes the diagonal speed the same as x and y (Length can only be 1)
        if self.direction.magnitude() > 0: #Cannot normalize a vector that is zero so must check if its greater than zero
            self.direction = self.direction.normalize()
        
        # Vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

        # Horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

    def update(self, dt):
        self.rect.x += self.direction.x
        posx = int(self.rect.x + self.direction.x)

        if self.status == 'right':
            frame = (posx//30) % len(self.animations['right'])
            self.image = self.animations['right'][frame]
        if self.status == 'left':
            frame = (posx//30) % len(self.animations['left'])
            self.image = self.animations['left'][frame]

        self.rect.y += self.direction.y
        posy = int(self.rect.y + self.direction.y)

        if self.status == 'up':
            frame = (posy//30) % len(self.animations['up'])
            self.image = self.animations['up'][frame]

        if self.status == 'down':
            frame = (posy//30) % len(self.animations['down'])
            self.image = self.animations['down'][frame]
        
        self.input()
        self.move(dt)
