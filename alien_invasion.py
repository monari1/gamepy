import sys
import pygame, sys
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""




    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen.fill(self.settings.bg_color)

        
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
        # make the most recent most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    """Make a game instance, and run the game loop"""
    ai = AlienInvasion()
    ai.run_game()