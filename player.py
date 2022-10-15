import pygame
from support import *
from settings import *
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.standcount = 0
        self.nextframe = 0
        self.status = 'down'
        self.frame_index = 0
        # uses direction as index for us to organize the files for the animations
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': []}

        sprite_sheet = Spritesheet("walkingss.png")
        sprite_sheet_idle = Spritesheet("idless.png")

        index = 0
        # adds down facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index, 0, 14, 16)
            self.animations['down'].append(image)
            index = index + 14
        # adds left facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index, 0, 14, 16)
            self.animations['left'].append(image)
            index = index + 14
        # adds right facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index, 0, 14, 16)
            self.animations['right'].append(image)
            index = index + 14
        # adds up facing animation sprites
        for x in range(4):
            image = sprite_sheet.get_image(index, 0, 14, 16)
            self.animations['up'].append(image)
            index = index + 14

        index2 = 0
        # adds downfacing idle animation
        for x in range(2):
            image = sprite_sheet_idle.get_image(index2, 0, 14, 16)
            self.animations['down_idle'].append(image)
            image = sprite_sheet_idle.get_image(index2, 0, 14, 17)
            self.animations['down_idle'].append(image)
            index2 = index2 + 14

        # adds leftfacing idle animation
        for x in range(2):
            image = sprite_sheet_idle.get_image(index2, 0, 14, 16)
            self.animations['left_idle'].append(image)
            image = sprite_sheet_idle.get_image(index2, 0, 14, 17)
            self.animations['left_idle'].append(image)
            index2 = index2 + 14
        # adds rightfacing idle animation
        for x in range(2):
            image = sprite_sheet_idle.get_image(index2, 0, 14, 16)
            self.animations['right_idle'].append(image)
            image = sprite_sheet_idle.get_image(index2, 0, 14, 17)
            self.animations['right_idle'].append(image)
            index2 = index2 + 14
        # adds upfacing idle animation
        for x in range(2):
            image = sprite_sheet_idle.get_image(index2, 0, 14, 16)
            self.animations['up_idle'].append(image)
            image = sprite_sheet_idle.get_image(index2, 0, 14, 17)
            self.animations['up_idle'].append(image)
            index2 = index2 + 14

        # Window Setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Movement Setup (Direction, Speed, etc.)
        self.direction = pygame.math.Vector2()  # Default value for Vector2 is (0, 0)
        # Sets the position of the player to be the center
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200  # Speed of the Player

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
            if self.status == 'down':
                self.status = 'down_idle'
            elif self.status == 'up':
                self.status = 'up_idle'

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
            if self.status == 'right':
                self.status = 'right_idle'
            elif self.status == 'left':
                self.status = 'left_idle'

    def move(self, dt):

        # Normalizing a Vector to set the diagonal direction to 1 instead of 2 which makes the diagonal speed the same as x and y (Length can only be 1)
        if self.direction.magnitude() > 0:  # Cannot normalize a vector that is zero so must check if its greater than zero
            self.direction = self.direction.normalize()

        # Vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

        # Horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

    def update(self, dt):
        # uses status of character to change image of frames left and right
        self.rect.x += self.direction.x
        posx = int(self.rect.x + self.direction.x)
        if self.status == 'right' or self.status == 'left':
            frame = (posx//30) % len(self.animations[self.status])
            self.image = self.animations[self.status][frame]

        # uses status of character to change image of frames for up and down
        self.rect.y += self.direction.y
        posy = int(self.rect.y + self.direction.y)
        if self.status == 'up' or self.status == 'down':
            frame = (posy//30) % len(self.animations[self.status])
            self.image = self.animations[self.status][frame]

        # uses status for animating idle
        if self.status == 'down_idle' or self.status == 'up_idle' or self.status == 'right_idle' or self.status == 'left_idle':
            # uses standcount to create a counter out of the dt
            self.standcount = self.standcount + dt
            # when standcount hit 1 or higher our nextframe will iterate through to create a new image
            # resets standcount to 0, animation occurs everytime standcount hits 1
            if self.standcount >= .5:
                self.nextframe = self.nextframe + 1
                self.image = self.animations[self.status][self.nextframe]
                self.standcount = 0
                # one nextframe hits 3 which is the last index of the animations array set standcount back to 0 and frames back to 0
                if self.nextframe == 3:
                    self.nextframe = 0

        self.input()
        self.move(dt)
