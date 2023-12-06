import pygame
import sys
from src.game import Game
import random

class Controller:
    def __init__(self):
        self.game = Game()

        self.num = random.randint(1, 10)


    """
    Second class is Controller. Basic overview on what keys get pressed and
    what happens in the game. (Make sure to change controller to something else)
    """

    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

        keys = pygame.key.get_pressed()
        self.game.player.movement(keys)

        if keys[pygame.K_SPACE] and not self.game.player.is_jumping:
            self.game.player.is_jumping = True

        if self.game.player.is_jumping:       
            self.game.player.jump()

    def run(self):
        if self.num > 5:
            print("hi")
        while self.game.running:
            self.game_events()
            self.game.update()
            self.game.draw()

        self.game.game_over()