import pygame, sys
from pygame import mixer
from arrow import Arrow

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Game")

#Background
BG = pygame.image.load("City.GIF")

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        UP_ARROW = Arrow(image="arrow.png", x_pos=600, y_pos=360)

        UP_ARROW.update(SCREEN)

pygame.display.update()

main_menu()
 