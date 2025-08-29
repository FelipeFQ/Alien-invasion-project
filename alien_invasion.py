import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from bullet import Bullet
from alien import Alien
from button import Button

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
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Set difficulty menu as False by default.
        self.show_difficulty_menu = False  

        # Make the Play and Level buttons.
        self._create_buttons()

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

    def _create_buttons(self):
        """Create the Play and Level buttons."""
        button_spacing = 20  
        button_width = 200
        total_width = 2 * button_width + button_spacing

        self.play_button = Button(self, "Play", x_offset=-total_width // 3,
                        instruction_text="Press 'P' to")
        self.level_button = Button(self, "Level", x_offset=total_width // 3,
                        instruction_text="Press 'L' to select starting")
        
        # Create difficulty buttons (hidden initially)
        difficulty_labels = ["Easy", "Medium", "Hard"]
        self.difficulty_buttons = []

        for index, label in enumerate(difficulty_labels):
            button = Button(
                self, label, 
                x_offset=total_width // 3,  # Same x as Level button
                width=180,  # Slightly smaller than Play button
                height=50
            )
            button.rect.y = self.level_button.rect.y + (index + 1) * 70  # Space them vertically
            button.msg_image_rect.center = button.rect.center 
            self.difficulty_buttons.append(button)  # Store in list

    def _start_game(self):
        """Start a new game by resetting stats and creating new game elements."""
        # Reset game setiings & statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.sb.prep_high_score() # prep the high score.


        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
    
    
    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user close the game save the high score.
                self.stats._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_menu_buttons(mouse_pos)
                

    def _check_menu_buttons(self, mouse_pos):
        """Start a new game when clicking Play or open the difficulty menu."""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self._start_game()

        elif self.level_button.rect.collidepoint(mouse_pos) and not self.show_difficulty_menu:
            self.show_difficulty_menu = True  # Show difficulty buttons

        for button in self.difficulty_buttons:
            if button.rect.collidepoint(mouse_pos) and self.show_difficulty_menu:
                selected_difficulty = button.msg  # Get the button text
                self.settings.set_difficulty(selected_difficulty)  # Call the new method
                self.show_difficulty_menu = False  # Hide menu after selection


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_d:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            # Move the ship up.
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            # Move the ship down.
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            self.stats._save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            if not self.game_active:
                self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            # Stop moving the ship to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            # Stop moving the ship to the left.
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            # Stop moving the ship up.
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            # Stop moving the ship down.
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add (new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet postions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision."""
        # Remove any bullets and aliens that have collied.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        
        if not self.aliens:
            # Destroy existing bullets and create nes fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for aliens-ship collitions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropiately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 4 * alien_width):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships leftn and update scoreboard.
            self.stats.ships_left -= 1 
            self.sb.prep_ships()

            # Get rid of any bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(1.0)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            
            if self.show_difficulty_menu:
                for button in self.difficulty_buttons:
                    button.draw_button()

            else:
                self.level_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
