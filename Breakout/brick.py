import pygame
import random

class Brick(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width , height):
        super().__init__()
        self.width = width
        self.height = height
        self.original_image = pygame.image.load("images/brick.png")
        self.image = pygame.transform.scale(self.original_image, (self.width , self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def update(self, surface):
        surface.blit(self.image, self.rect)

    def check_collision(self, ball):
        ball_coordenates = (ball.pos_x, ball.pos_y - ball.radius)
        if self.rect.collidepoint(ball_coordenates):
            ball.bounce_sound.play()
            ball.speed_y *= -1
            ball.speed_x *= random.choice([1,-1])
            self.kill()
        
    
