import pygame
from colors import COLORS
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, radius, speed):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.speed_x = speed
        self.speed_y = speed
        self.throw_angle = math.pi
        self.percentage = 0.5
        self.bounce_sound = pygame.mixer.Sound("audio/sound/ball_sound.wav")
        self.ball_surface = pygame.Surface((self.radius * 2, self.radius * 2))
        self.ball_rect = self.ball_surface.get_rect()
        self.ball_rect.center = (self.pos_x, self.pos_y)

    def update(self, surface):
        self.ball_surface.fill(COLORS.GREEN)
        pygame.draw.circle(self.ball_surface, COLORS.WHITE, (self.radius, self.radius), self.radius)
        surface.blit(self.ball_surface, (self.pos_x - self.radius, self.pos_y - self.radius))

        
        
    def move(self, screen_height):
        self.pos_y -= math.sin(self.percentage * self.throw_angle) * self.speed_y
        self.pos_x += math.cos(self.percentage * self.throw_angle) * self.speed_x
        if self.pos_y > screen_height  + 200:
            self.kill()
            
    def check_collision(self, upper_surface_height, surface_width, player):
        if self.pos_y - self.radius <= upper_surface_height:
            self.bounce_sound.play()
            self.speed_y *= -1

        if self.pos_x + self.radius >= surface_width or self.pos_x - self.radius <= 0:
            self.bounce_sound.play()
            self.speed_x *= -1

        if player.collidepoint(self.pos_x, self.pos_y + self.radius):
            self.bounce_sound.play()
            self.speed_y *= -1
    	    
            '''the self.speed_x need to be positive integer before it gets multiplied by the cos and sin angle '''
            self.speed_x = abs(self.speed_x )  
    
            self.percentage = 1 - (self.pos_x - player.x) / player.width
            if self.percentage < 0.2: self.percentage = 0.2
            if self.percentage > 0.8: self.percentage = 0.8



