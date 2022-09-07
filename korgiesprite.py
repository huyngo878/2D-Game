import pygame
import sys
import os

pygame.init()
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run1.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run2.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run3.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run4.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run5.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run6.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run7.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run8.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run9.png')))
        self.sprites.append(pygame.image.load(os.path.join('maps', 'Hobbit - run10.png')))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False

        self.image = self.sprites[int(self.current_sprite)]


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sprite Test")

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()       
        if event.type == pygame.KEYDOWN:
            player.animate()



    #draw
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)