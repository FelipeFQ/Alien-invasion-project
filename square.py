import pygame
from pygame.sprite import Sprite

class Square(Sprite):
    """A class to represent the squared for training sessions."""

    def __init__(self, ai_game):
        """Initialize the square and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create the square with dimensions from settings
        self.rect = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.square_color 

        # Start the square on the right center of the screen.
        self.rect.right = self.screen_rect.right - self.settings.square_width
        self.rect.centery = self.screen_rect.centery

        # Store the square's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the square up or down and left or right."""
        self.y += self.settings.square_speed * self.settings.y_square_direction
        self.x += self.settings.square_speed * self.settings.x_square_direction
        
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_square(self):
        """Draw the square on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect, width=3)