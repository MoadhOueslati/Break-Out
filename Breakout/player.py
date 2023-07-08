import pygame
from colors import COLORS

class Player:
    def __init__(self, pos_x , pos_y, width , height, color):
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.throwable= True
        self.ball_thrown = False


    def update(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.move()
        self.throw_ball()

    def move(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        
    def throw_ball(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.throwable:
            self.throwable = False 
            self.ball_thrown = True
            

        





    