import pygame
import os
from network import Network
##using the class "Network" from the file network.py
# from network import Network

ani = 6 #animation cycles
FPS = 60
ALPHA = 0
WIDTH = 800
HEIGHT = 600
VELOCITY = 3
BULLET_VELOCITY = 6
GUN_BULLET = 16


MAP_IMAGE = pygame.image.load(os.path.join('maps', 'map1.png'))


##size of screen
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
#Name of Application
pygame.display.set_caption("Client")

clientNum = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, color):
        super().__init__()
       
        self.images = []
        for i in range ( 1, 2):
            img = pygame.image.load(os.path.join('maps','Hobbit - attack' + str(i) + '.png')).convert() #takes in image and places it into array
            self.images.append(img)
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.center = [pos_x,pos_y]
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 40 # count frames

    def control(self,x, y):
        #player movement
        self.movex += x
        self.movey += y

    def update(self):
        #updates position of sprite
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        


def drawDisplay(DISPLAY):
    DISPLAY.blit(MAP_IMAGE, (-50,0))
    
    # player.draw(DISPLAY)
    # # player2.draw(DISPLAY)
    # pygame.display.update()

def main():
    run = True
    # n = Network()

    c = Player(50, 50, 100, 100, (255,255,255))
    
    player_group = pygame.sprite.Group()
    player_group.add(c)
    steps = 5
 

    clock = pygame.time.Clock()

    while run:

  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #inputs for when the key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    c.control(-steps,0) #uses steps to control how much velocity when holding key down
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    c.control(steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    c.control(0,-steps)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    c.control(0,steps)
                
            #inputs for when the key is let go of
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    c.control(steps,0) #use opposite steps as keydown so that momentum is put to 0 and character wont keep moving
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    c.control(-steps,0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    c.control(0,steps)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    c.control(0,-steps)

                if event.key == ord('q'):
                    pygame.quit()
                    run = False    
        
        pygame.display.flip()


        c.update()
        drawDisplay(DISPLAY)
        player_group.draw(DISPLAY)
        clock.tick(FPS)

if __name__ == "__main__":
    main()