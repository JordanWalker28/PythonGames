import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
          self.rect.y = 400
          
    def moveLeft(self, pixels, paddle):
        self.rect.x -= pixels
        if paddle == "paddleA":
            if self.rect.x < 20:
                self.rect.x = 20
        elif paddle == "paddleB":
            if self.rect.x < 350:
                self.rect.x = 350
        else:
            if self.rect.x < 0:
                self.rect.x = 0
            
    def moveRight(self, pixels, paddle):
        self.rect.x += pixels
        if paddle == "paddleA":
            if self.rect.x > 350:
                self.rect.x = 350
        elif paddle == "paddleB":
            if self.rect.x > 680:
                self.rect.x = 680
        else:
            if self.rect.x > 700:
                self.rect.x = 700
