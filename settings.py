class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (12, 13 ,30) 
        
        # Ship settings
        self.ship_speed = 3

        # Bullets settings
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 249, 25)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1