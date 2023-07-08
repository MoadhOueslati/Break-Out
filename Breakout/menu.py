import pygame
import sys
from colors import COLORS
from button import Button

from main import Game

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ORIGINAL_MENU_BACKGROUND = pygame.image.load("images/menu_background.jpg")
MENU_BACKGROUND = pygame.transform.scale(ORIGINAL_MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Font type & size
def get_font(size):
    return pygame.font.SysFont(None, size)

def options():
    pygame.display.set_caption("options")

    #Title setup
    TITLE_TEXT = get_font(150).render("Options", True, COLORS.BLACK)
    TITLE_RECT = TITLE_TEXT.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//6))    

    #back button setup
    BACK_BUTTON_WIDTH = 250 
    BACK_BUTTON_HEIGHT = 80
    BACK_BUTTON_POS_X = (SCREEN_WIDTH // 2) - (BACK_BUTTON_WIDTH // 2)
    BACK_BUTTON_POS_Y = SCREEN_HEIGHT - BACK_BUTTON_HEIGHT - 50 
    back_button = Button(BACK_BUTTON_POS_X, BACK_BUTTON_POS_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT, COLORS.GREEN, "BACK", None, get_font(80))

    #music setup
    MUSIC_TEXT = get_font(100).render("music :", True, COLORS.BLACK)
    MUSIC_RECT = MUSIC_TEXT.get_rect(center = (350,300))
    MUSIC_IMAGE = pygame.image.load("images/music_icon.png")
    MUSIC_ICON = pygame.transform.scale(MUSIC_IMAGE, (100,100))
    music_button = Button(550, 250, 100, 100, None, None, MUSIC_ICON, None)

    #sound setup
    SOUND_TEXT = get_font(100).render("sound :", True, COLORS.BLACK)
    SOUND_RECT = SOUND_TEXT.get_rect(center = (350,450))
    SOUND_IMAGE = pygame.image.load("images/sound_icon.png")
    SOUND_ICON = pygame.transform.scale(SOUND_IMAGE, (100,100))
    sound_button = Button(550, 400, 100, 100, None, None, SOUND_ICON, None)

    while True:
        SCREEN.blit(MENU_BACKGROUND, (0,0))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        #draw texts 
        SCREEN.blit(MUSIC_TEXT, MUSIC_RECT)
        SCREEN.blit(SOUND_TEXT, SOUND_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_button.is_clicked():
                    print("music on/off")
                if sound_button.is_clicked():
                    print("sound on/off")
                if back_button.is_clicked():
                    return

        #Draw buttons
        back_button.draw(SCREEN)
        music_button.draw(SCREEN)
        sound_button.draw(SCREEN)
    
        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")
    #Title setup
    TITLE_TEXT = get_font(200).render("Break Out", True, COLORS.LIGHT_YELLOW)
    TITLE_RECT = TITLE_TEXT.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//6))
    
    #Buttons building
    BUTTON_WIDTH = 300 
    BUTTON_HEIGHT = 100
    BUTTON_SPACING = 130
    BUTTON_POS_X = (SCREEN_WIDTH // 2) - (BUTTON_WIDTH // 2)
    BUTTON_POS_Y = 250
    
    play_button = Button(BUTTON_POS_X, BUTTON_POS_Y, BUTTON_WIDTH, BUTTON_HEIGHT, COLORS.GREEN, "PLAY", None, get_font(80))
    options_button = Button(BUTTON_POS_X, BUTTON_POS_Y + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT, COLORS.GREEN, "OPTIONS", None, get_font(80))
    quit_button = Button(BUTTON_POS_X, BUTTON_POS_Y + BUTTON_SPACING * 2, BUTTON_WIDTH, BUTTON_HEIGHT, COLORS.GREEN, "QUIT", None, get_font(80))

    buttons = [play_button, options_button, quit_button]

    while True:
        SCREEN.blit(MENU_BACKGROUND, (0,0))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        #Drawing Buttons
        for button in buttons:
            button.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked():
                    game = Game(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
                    game.run()
                elif options_button.is_clicked():
                    options()
                elif quit_button.is_clicked():
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#initiating main menu
main_menu()