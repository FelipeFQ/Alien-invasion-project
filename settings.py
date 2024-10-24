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
        self.bullet_color = (228, 57, 57)
        self.bullets_allowed = 5