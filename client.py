import pygame
import os
import sys
##using the class "Network" from the file network.py
from network import Network

FPS = 60
WIDTH = 800
HEIGHT = 600
VELOCITY = 3
BULLET_VELOCITY = 6
GUN_BULLET = 16
MAP_IMAGE = pygame.image.load(os.path.join('maps', 'map1.png'))
CHARACTER1 = pygame.image.load(os.path.join('maps', 'Hobbit - attack1.png'))

##size of screen
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
#Name of Application
pygame.display.set_caption("Client")

clientNum = 0

class playerGani(pygame.sprite.Sprite):
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

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, DISPLAY):
        pygame.draw.rect(DISPLAY, self.color, self.rect)

    def char_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: ## and self.x - VELOCITY > - 25: ##left
            self.x -= VELOCITY
        if keys_pressed[pygame.K_d]: ## and self.x + VELOCITY + self.width< WIDTH - 20: ##right
            self.x += VELOCITY
            player.animate()
        if keys_pressed[pygame.K_w]: ## and self.y - VELOCITY > - 25: ##up
            self.y -= VELOCITY
        if keys_pressed[pygame.K_s]: ##and self.y + VELOCITY + self.height < HEIGHT - 20: ##down
            self.y += VELOCITY
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

##takes in number in string value and convert them into tup of ints for char position
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def drawDisplay(DISPLAY, player, player2):

    DISPLAY.blit(MAP_IMAGE, (-50,0))
    moving_sprites.draw(DISPLAY)
    moving_sprites.update()
    player.draw(DISPLAY)
    
    pygame.display.update()

moving_sprites = pygame.sprite.Group()
player = playerGani(100,100)
moving_sprites.add(player)

def main():
    run = True
    n = Network()
    #startPos = read_pos(n.getPos()) 
    c = Player(0, 0, 20, 20, (0,255,0))
    c2 = Player(0, 0, 20, 20, (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        #c2Pos = read_pos(n.send(make_pos((c.x, c.y))))
        #c2.x = c2Pos[0]
        #c2.y= c2Pos[1]
        #c2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        c.char_movement()
        drawDisplay(DISPLAY, c, player)

if __name__ == "__main__":
    main()