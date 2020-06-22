import pygame
from dinosaur import Dinosaur
from obstacle import Obstacle

pygame.init()

size = width, height = 800, 600
gameDisplay = pygame.display.set_mode(size)

xPos = 0
yPos = 0
black = 0,0,0
Ground_Height = height - 100

dinsaur = Dinosaur(Ground_Height)

lastFrame = pygame.time.get_ticks()

import random
MINGAP = 200
VELOCITY = 300
MAXGAP = 600

obstacles = []

num_of_obstacles = 4
lastObstacle = width

obstaclesize = 20

for i in  range(4):
    lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()
    obstacles.append(Obstacle(lastObstacle,size,Ground_Height))

white = 255,255,255

while True:
    t = pygame.time.get_ticks()
    deltaTime = (t-lastFrame)/1000.0
    lastFrame = t

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinsaur.jump()

    gameDisplay.fill(black)

    dinsaur.update(deltaTime)
    dinsaur.draw(gameDisplay)

    for obs in obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)
        if (obs.checkOver()):
            lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()
            obs.x = lastObstacle

    lastObstacle -= VELOCITY * deltaTime

    pygame.draw.rect(gameDisplay, white, [0,Ground_Height , width, height - Ground_Height])
    pygame.draw.rect(gameDisplay, white, [xPos, yPos, 40, 50])
    xPos += 1
    yPos += 1
    pygame.display.update()  # updates the screen 