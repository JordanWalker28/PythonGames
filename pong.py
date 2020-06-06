import pygame
from paddle import Paddle

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (57,200,20)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(GREEN, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(GREEN, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

GameActive = True
 
clock = pygame.time.Clock()

while GameActive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              GameActive = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
        
    all_sprites_list.update()

    screen.fill(BLACK)

    pygame.draw.line(screen, GREEN, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, WHITE, [0, 1], [700, 1], 5)

    all_sprites_list.draw(screen)
    
    pygame.display.flip()
     
    clock.tick(60)

pygame.quit()
