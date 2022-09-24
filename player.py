import pygame
from settings import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('maps', 'Hobbit - run' + str(i) + '.png')).convert_alpha() #Takes in image
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()

        def input(keys):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.direction.y = -1

