import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near to the top right of the screen.
        self.rect.x = self.settings.screen_width - 2 * self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return(self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)