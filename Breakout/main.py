import pygame
import sys
from colors import COLORS
from player import Player
from ball import Ball
from brick import Brick


class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.clock = pygame.time.Clock()
        self.FPS = 60
        pygame.display.set_caption("Break Out")

        self.UPPER_SCREEN_HEIGHT = self.HEIGHT//6
        self.UPPER_SCREEN = pygame.Surface((self.WIDTH, self.UPPER_SCREEN_HEIGHT))

        self.BOTTOM_SCREEN_HEIGHT = self.HEIGHT - self.UPPER_SCREEN_HEIGHT
        self.BOTTOM_SCREEN = pygame.Surface((self.WIDTH, self.BOTTOM_SCREEN_HEIGHT))


        self.original_background_image = pygame.image.load("images/game_background.jpg")
        self.background_image = pygame.transform.scale(self.original_background_image, (self.WIDTH, self.HEIGHT))
        self.game_over = False
        self.player_width = 150
        self.player_height = 10
        self.player = Player(self.WIDTH//2 - self.player_width//2, self.HEIGHT - self.player_height * 3, self.player_width, self.player_height, COLORS.WHITE)

        #ball group build
        self.ball_group = pygame.sprite.Group()
        self.ball_amount = 30

        #brick group build
        self.brick_group = pygame.sprite.Group()
        self.brick_width = 90
        self.brick_height = 30
        self.brick_amount = self.WIDTH // self.brick_width

        self.brick_spacing = (self.WIDTH - (self.brick_amount * self.brick_width)) / (self.brick_amount + 1)
        self.brick_pos_x = self.brick_spacing
        self.brick_pos_y = 10
        self.spawn_bricks()


    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update_screens()
            self.update()
            pygame.display.update()
            self.clock.tick(self.FPS)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_screens(self):
        self.screen.blit(self.UPPER_SCREEN, (0,0))
        self.screen.blit(self.BOTTOM_SCREEN, (0, self.UPPER_SCREEN_HEIGHT))
        self.BOTTOM_SCREEN.blit(self.background_image, (0,0))
        pygame.draw.rect(self.UPPER_SCREEN, COLORS.WHITE, (0, self.UPPER_SCREEN_HEIGHT- 5, self.WIDTH, 5))
    

    def update(self):
        #update the player 
        self.player.update(self.screen)
        #update the balls
        self.ball_group.update(self.screen)
        #update the bricks
        self.brick_group.update(self.screen)


        if len(self.ball_group) == 0:
            self.spawn_balls()
            self.player.throwable = True
            self.player.ball_thrown = False

        if not self.player.ball_thrown:   #dont throw ball if player havent press shoot yet
            for ball in self.ball_group:
                ball.pos_x = self.player.rect.centerx
        else: 
            for ball in self.ball_group:
                ball.move(self.HEIGHT)
                ball.check_collision(self.UPPER_SCREEN_HEIGHT, self.WIDTH, self.player.rect)

        
        for brick in self.brick_group:
            for ball in self.ball_group:
                brick.check_collision(ball)
        

    def spawn_balls(self):
        for _ in range(self.ball_amount):
            ball_radius = 10
            ball = Ball(self.player.rect.centerx , (self.HEIGHT - self.player_height * 3) - ball_radius , radius=ball_radius, speed = 15)
            self.ball_group.add(ball)

    def spawn_bricks(self):
        for _ in range(16):
            for _ in range(self.brick_amount):
                brick = Brick(self.brick_pos_x , self.UPPER_SCREEN_HEIGHT + self.brick_pos_y, self.brick_width, self.brick_height)
                self.brick_pos_x += self.brick_width + self.brick_spacing
                self.brick_group.add(brick)
            self.brick_pos_x = self.brick_spacing
            self.brick_pos_y += self.brick_height + self.brick_spacing

