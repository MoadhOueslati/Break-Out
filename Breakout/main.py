import pygame
import sys
from colors import COLORS
from player import Player

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Break Out")

        self.original_background_image = pygame.image.load("images/game_background.jpg")
        self.background_image = pygame.transform.scale(self.original_background_image, (self.width, self.height))
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.screen.blit(self.background_image,(0,0))
            self.handle_events()
            pygame.display.update()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
