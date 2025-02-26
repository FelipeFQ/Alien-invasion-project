import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (253, 255, 73)
        self. font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        ship_image = pygame.image.load('images/Gimages/ship0.bmp') # Load the original ship image
        original_width, original_height = ship_image.get_size()
        new_width = original_width // 2  # Reduce width by half
        new_height = original_height // 2  # Reduce height by half

        scaled_ship_image = pygame.transform.scale(ship_image, (new_width, new_height))
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = scaled_ship_image  # Assign the scaled image to ship.image
            ship.rect = ship.image.get_rect()  # Update the ship's rect
            ship.rect.x = 20+ ship_number * (ship.rect.width + 5)
            ship.rect.y = 20
            self.ships.add(ship)



    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen,
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score, level, and ships to the screen."""
        self.screen.blit (self.score_image, self.score_rect)
        self.screen.blit (self.high_score_image, self.high_score_rect)
        self.screen.blit (self.level_image, self.level_rect)
        self.ships.draw(self.screen)

