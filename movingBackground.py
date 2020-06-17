import pygame

pygame.init()

screen_width = 800
screen_height = 600

display = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

bg = pygame.image.load('background.jpg').convert()
bgx = 0
bgx2 = bg.get_width()

run = True
speed = 30


class Player:
    pass
    
def redrawWin():
    display.blit(bg, (bgx, 0))
    display.blit(bg, (bgx2, 0))
    pygame.display.update()


while run:
    redrawWin()
    clock.tick(speed)
    bgx -= 6.4
    bgx2 -= 6.4
    if bgx < bg.get_width() * -1:
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:
        bgx2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

