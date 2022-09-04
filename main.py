from operator import truediv
import pygame
import os
pygame.init()

##screen sized W, H
BULLET_COLOR = (255, 0, 0)
WIDTH, HEIGHT = 900, 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
##rename the application
pygame.display.set_caption("2Dgame")
#hello
##Global frames per second
FPS = 60
CHAR_H, CHAR_W = 20, 17
VELOCITY = 3
BULLET_VELOCITY = 6
GUN_BULLET = 16

CHAR1_HIT = pygame.USEREVENT + 1
CHAR2_HIT = pygame.USEREVENT + 2

MAP_IMAGE = pygame.image.load(os.path.join('maps', 'map1.png'))
CHARACTER1 = pygame.image.load(os.path.join('maps', 'Hobbit - attack1.png'))

##function for draw dispay
def Dwindow(char1, char1_bullets):
    DISPLAY.blit(MAP_IMAGE, (-50,0))
    DISPLAY.blit(CHARACTER1, (char1.x, char1.y))

    for bullet in char1_bullets:
        pygame.draw.rect(DISPLAY, BULLET_COLOR, bullet)
    
    pygame.display.update()

##character movement
def char_movement(keys_pressed, char1):
    if keys_pressed[pygame.K_a] and char1.x - VELOCITY > - 25: ##left
        char1.x -= VELOCITY
    if keys_pressed[pygame.K_d] and char1.x + VELOCITY + char1.width< WIDTH - 20: ##right
        char1.x += VELOCITY
    if keys_pressed[pygame.K_w] and char1.y - VELOCITY > - 25: ##up
        char1.y -= VELOCITY
    if keys_pressed[pygame.K_s] and char1.y + VELOCITY + char1.height < HEIGHT - 20: ##down
        char1.y += VELOCITY

##bullet register
def bullet_damage(char1_bullets, char1):
    for bullet in char1_bullets:
        bullet.x += BULLET_VELOCITY
        if char1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CHAR2_HIT))
            char1_bullets.remove(bullet)


def main():
    char1 = pygame.Rect(100, 100, CHAR_W, CHAR_H)

    char1_bullets = []

    clock = pygame.time.Clock()
    ##run until the game close
    run = True
    while run:
        ##clock.tick controls the amount of time the game is being refreshed
        clock.tick(FPS)
        ##If user quit close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j and len(char1_bullets) < GUN_BULLET:
                    bullet = pygame.Rect(char1.x + char1.width, char1.y + char1.height//2 , 10, 5)
                    char1_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed, char1)

        bullet_damage(char1_bullets, char1)

        Dwindow(char1, char1_bullets)

    pygame.quit()

if __name__ == "__main__":
    main()