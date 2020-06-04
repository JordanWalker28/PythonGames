import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

GameActive = True
 
clock = pygame.time.Clock()

while GameActive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              GameActive = False
 

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, WHITE, [0, 1], [700, 1], 5)

    pygame.display.flip()
     
    clock.tick(60)

pygame.quit()
