import pygame
import random
import sys

from controller import Controller
from game import Game
from player import Player

WIDTH =800
HEIGHT = 600
FPS = 60
WHITE = "white"
RED = "red"
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50

is_jumping = False
block_jump = 10
score = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BOX_WIDTH = 100
BOX_HEIGHT = 50

BLACK = "black"
RED = "red"
BLUE = "blue"

value = None
running = True

##############################################################

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
red_rect = pygame.Rect(275, 290, BOX_WIDTH, BOX_HEIGHT)
blue_rect = pygame.Rect(425, 290, BOX_WIDTH, BOX_HEIGHT)
pygame.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if red_rect.collidepoint(event.pos):
                    value = 1
                    running = False
                elif blue_rect.collidepoint(event.pos):
                    value = 2
                    running = sys.exit()

    screen.fill(BLACK) 
    pygame.draw.rect(screen, RED, red_rect)
    pygame.draw.rect(screen, BLUE, blue_rect)
    font = pygame.font.Font(None, 48)
    text = font.render("Welcome to falling Rectangles!", True, "white")
    screen.blit(text, (150, 150))
    font = pygame.font.Font(None, 48)
    text = font.render("Play", True, "white")
    screen.blit(text, (290, 300))
    font = pygame.font.Font(None, 48)
    text = font.render("Exit", True, "white")
    screen.blit(text, (440, 300))
    pygame.display.flip()

############################################################################

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    that = Controller() # 4
    that.run() #run(that)
    this = Controller() # 8
    this.run() #run(this)


def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/



