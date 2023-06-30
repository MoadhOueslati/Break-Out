import pygame
from colors import COLORS

class Button:
    def __init__(self, pos_x, pos_y, width, height, bg_color=None, text=None, image=None, font=None):
        self.image = image
        self.RECT = pygame.Rect(pos_x, pos_y, width, height)
        self.BG_COLOR = bg_color
        self.TEXT = text
        self.FONT = font

    def draw(self, surface):
        if self.BG_COLOR:
            pygame.draw.rect(surface, self.BG_COLOR, self.RECT)
        if self.image:
            image_rect = self.image.get_rect(center=self.RECT.center)
            surface.blit(self.image, image_rect)
        if self.TEXT and self.FONT:
            text_surface = self.FONT.render(self.TEXT, True, COLORS.WHITE)
            text_rect = text_surface.get_rect(center=self.RECT.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self):
        return self.RECT.collidepoint(pygame.mouse.get_pos())
