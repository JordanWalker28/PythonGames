import pygame

dinocolor = 255,255,255

dinoHeight = 40
dinoWidth = 20

class Dinosaur:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = dinoHeight
        self.width = dinoWidth
        self.surfaceHeight = surfaceHeight

    def jump(self):
        if(self.y == 0):
            self.yvelocity = 300

    def update(self,deltaTime):
        self.yvelocity += 500 * deltaTime
        if self.y < 0:
            self.y = 0
            self.yvelocity = 0

    def draw(self, display):
        pygame.draw.rect(display,dinocolor,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])