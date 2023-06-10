import pygame

class Ship:
    def __init__(self, ai_game):
        # initialize the ship and sets its position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load the ship image
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        # draw the ship at its current location
        self.screen_blit(self.image, self.rect)
        