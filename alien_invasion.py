import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from square import Square

class AlienInvasion:
    """Overall to manage game assets ang behaviors"""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.square = pygame.sprite.Group()

        self._create_square()

        # Start Alien Invasion in an active state.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_square()

            self._update_screen()
            self.clock.tick(60)
            
    
    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_DOWN:
            # Move the ship down.
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            # Move the ship up.
            self.ship.moving_up = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            # Stop moving the ship down.
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            # Stop moving the ship up.
            self.ship.moving_up = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add (new_bullet)

    def _update_bullets(self):
        """Update positiion of bullets and get rid of the old bullets."""
        # Update bullet's positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

        
        self._check_bullet_square_collitions()

    def _check_bullet_square_collitions(self):
        """Respond to bullet-square collitions."""
        # Remove any bullets and squares that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.square, True, True)
        
        if not self.square:
            # Destroy existing bullets and create new square.
            self.bullets.empty()
            self._create_square()

    def _update_square(self):
        """Check if the square is at an edge, then update positions."""
        self._check_square_edges()
        self.square.update()

    def _create_square(self):
        """Create the training square."""
        new_square = Square(self)
        self.square.add(new_square)


    def _check_square_edges(self):
        """Check if the square has reached an edge and trigger direction change."""
        for square in self.square.sprites():
            hit_x = False
            hit_y = False

        if square.rect.right >= self.settings.screen_width or square.rect.left <= 0:
            hit_x = True  # Change X direction
        if square.rect.bottom >= self.settings.screen_height or square.rect.top <= 0:
            hit_y = True  # Change Y direction

        if hit_x or hit_y:
            self._change_square_direction(hit_x, hit_y)


    def _change_square_direction(self, hit_x, hit_y):
        """Reverse the square's movement direction."""
        if hit_x:
            self.settings.x_square_direction *= -1  # Reverse X movement only
        if hit_y:
            self.settings.y_square_direction *= -1  # Reverse Y movement only
    

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # ✅ Correct way to draw the square since it doesn't have an `image`
        for square in self.square.sprites():
            square.draw_square()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
