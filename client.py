import pygame
import os
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
    player.draw(DISPLAY)
    player2.draw(DISPLAY)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos()) 
    c = Player(startPos[0], startPos[1], 20, 20, (0,255,0))
    c2 = Player(0, 0, 20, 20, (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        c2Pos = read_pos(n.send(make_pos((c.x, c.y))))
        c2.x = c2Pos[0]
        c2.y= c2Pos[1]
        c2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        c.char_movement()
        drawDisplay(DISPLAY, c, c2)

if __name__ == "__main__":
    main()