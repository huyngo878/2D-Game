import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Window Setup
        self.image = pygame.Surface((16, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        # Movement Setup (Direction, Speed, etc.)
        self.direction = pygame.math.Vector2() # Default value for Vector2 is (0, 0)
        self.pos = pygame.math.Vector2(self.rect.center) #Sets the position of the player to be the center
        self.speed = 450 #Speed of the Player

    def import_assets(self):
        self.animations = {}

        # #self.import_assets()
        # self.status = 'down_idle'
        # self.frame_index = 0

        # # Window Setup
        # self.image = self.animations[self.status][self.frame_index]
        # self.rect = self.image.get_rect(center = pos)

        # # Movement Setup (Direction, Speed, etc.)
        # self.direction = pygame.math.Vector2() # Default value for Vector2 is (0, 0)
        # self.pos = pygame.math.Vector2(self.rect.center) #Sets the position of the player to be the center
        # self.speed = 450 #Speed of the Player

    # def import_assets(self):
    #     self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 
    #                        'right_idle':[], 'left_idle': [], 'up_idle': [], 'down_idle': []}

    #     for animation in self.animations.keys():
    #         full_path = '../graphics/NPCs/NPC 01_idle (16x24).png' + animation
    #         self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0



        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
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
        self.input()
        self.move(dt)
