import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an active state.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

        if not self.aliens:
            # Destroy exiting bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

        
        self._check_bullet_alien_collitions()

    def _check_bullet_alien_collitions(self):
        """Respond to bullet-alien collitions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the left side of the screen.
        self._check_aliens_leftside()

    def _ship_hit(self):
        """Respond to the ship beeing hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships left.
            self.stats.ship    # Decrement ships left.
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(2.0)

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(2.0)
        else:
            self.game_active = False

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create and alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien height and one alien width.
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size

        current_y, current_x = alien_height, self.settings.screen_width - 2* alien_width
        while current_x > ( 5 * alien_width):
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_y, current_x)
                current_y += 2 * alien_height

            # Finished a row: reset y value, and decrease x value
            current_y = alien_height
            current_x -= 2 * alien_width
        
    def _create_alien(self, y_position, x_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.y = y_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Responde appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Advance the etire fleet and change fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_advance_speed
        self.settings.fleet_direction *= -1 

    def _check_aliens_leftside(self):
        """check if any aliens have reach the left side of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
